import json
import re

import requests
from scrapy.http import HtmlResponse


def recipe_data(url):
    try:
        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
        response = requests.get(url=url, headers=header)
        if response.status_code == 200:
            # response = requests.request("GET", url)
            a = response.text
            api_response = dict()
            response_s = HtmlResponse(url=url, body=a, headers=header, encoding='utf-8')
            page_text = response_s.xpath('//script[@type="application/ld+json"]/text()').extract()
            data = {}
            if page_text != []:
                for rec in page_text:
                    data_json_list = json.loads(rec.strip())
                    if type(data_json_list) == list:
                        for data_json in data_json_list:
                            if '@graph' in data_json.keys():
                                for data1 in data_json['@graph']:
                                    if data1['@type'] == "Recipe":
                                        data = data1
                            else:
                                if data_json['@type'] == "Recipe":
                                    data = data_json
                    else:
                        if '@graph' in data_json_list.keys():
                            for data1 in data_json_list['@graph']:
                                if data1['@type'] == "Recipe":
                                    data = data1
                        else:
                            if data_json_list['@type'] == "Recipe":
                                data = data_json_list
                    if data != {}:
                        api_response['URL'] = url
                        try:api_response['Name'] = data['name']
                        except:api_response['Name'] = ''
                        try:api_response['image'] = data['image']['url']
                        except:api_response['image'] = ''
                        try:api_response['Description'] = data['description']
                        except:api_response['Description'] = ''
                        try:api_response['prepTime'] = data['prepTime']
                        except:api_response['prepTime'] = ''
                        try:api_response['cookTime'] = data['cookTime']
                        except:api_response['cookTime'] = ''
                        try:api_response['totalTime'] = data['totalTime']
                        except:api_response['totalTime'] = ''
                        try:api_response['keywords'] = data['keywords']
                        except:api_response['keywords'] = ''
                        try:api_response['recipeCategory'] = data['recipeCategory']
                        except:api_response['recipeCategory'] = []
                        try:api_response['recipeCuisine'] = data['recipeCuisine']
                        except:api_response['recipeCuisine'] = []
                        try:api_response['recipeIngredient'] = data['recipeIngredient']
                        except:api_response['recipeIngredient'] = []
                        try:
                            recipeInstructions = []
                            if type(data['recipeInstructions']) == list:
                                for recipe_instruct in data['recipeInstructions']:
                                    if "text" in recipe_instruct.keys():
                                        recipeInstructions.append(recipe_instruct['text'])
                                    else:
                                        for itemlist in recipe_instruct['itemListElement']:
                                            recipeInstructions.append(itemlist['text'])
                            else:
                                recipeInstructions.append(data['recipeInstructions'])
                            api_response['recipeInstructions'] = recipeInstructions
                        except:api_response['recipeInstructions'] = []
                        try:api_response['nutrition'] = data['nutrition']
                        except:api_response['nutrition'] = []
                        break
                    else:
                        api_response['URL'] = url
                        try:api_response['Name'] = data_json_list['headline']
                        except:api_response['Name'] = ''
                        try:api_response['image'] = data_json_list['image']['url']
                        except:api_response['image'] = ''
                        api_response['Description'] = ''
                        api_response['prepTime'] = ''
                        api_response['cookTime'] = ''
                        api_response['totalTime'] = ''
                        api_response['keywords'] = ''
                        api_response['recipeCategory'] = ''
                        api_response['recipeCuisine'] = ''
                        api_response['recipeIngredient'] = ''
                        api_response['recipeInstructions'] = []
                        api_response['nutrition'] = []
            else:
                api_response['URL'] = url
                try:
                    xpath_name = '(//h1/*[@itemprop="name"]|//h1/span/span|//h2/ul/li|//div[@id="recipe-title"]/h2|//h3[@class="post-title entry-title"]|//h3/strong/strong|//h1[@class="fn"]|//h1[@class="entry-title"])'
                    api_response['Name'] = response_s.xpath(f'{xpath_name}/text()').extract_first(default='').strip()
                except:
                    api_response['Name'] = ''
                try:
                    xpath_image = '(//img[@class="recipe-image"]|//div[@class="block_item"]/div|//p/a/img|//div[@class="post-thumbnail"]/img|//div/a/img|//img)'
                    match = url.split('/')[2]
                    image_url = response_s.xpath(f'{xpath_image}/@src|@data-pin-media').extract_first(default='').strip()
                    if match not in image_url and 'http' not in image_url and image_url != '':
                        image_url = match+image_url
                    if 'Subscribe-button' in image_url:
                        image_url = ''
                    api_response['image'] = image_url
                except:
                    api_response['image'] = ''
                try:api_response['Description'] = ''.join(response_s.xpath('//*[@id="recipe_description"]//text()').extract()).strip()
                except:api_response['Description'] = ''
                try:api_response['prepTime'] = response_s.xpath('//*[@itemprop="prepTime"]/@datetime').extract_first().strip()
                except:api_response['prepTime'] = ''
                try:api_response['cookTime'] = response_s.xpath('//*[@itemprop="cookTime"]/@datetime').extract_first().strip()
                except:api_response['cookTime'] = ''
                try:api_response['totalTime'] = response_s.xpath('//*[@itemprop="totalTime"]/@datetime').extract_first().strip()
                except:api_response['totalTime'] = ''
                try:api_response['keywords'] = response_s.xpath('//*[@itemprop="keywords"]/@content').extract_first().strip()
                except:api_response['keywords'] = ''
                try:api_response['recipeCategory'] = response_s.xpath('//*[@itemprop="recipeCategory"]/span/text()').extract()
                except:api_response['recipeCategory'] = []
                try:api_response['recipeCuisine'] = response_s.xpath('//*[@itemprop="recipeCuisine"]/span/text()').extract()
                except:api_response['recipeCuisine'] = []
                try:
                    recipeIngredient_list = []
                    recipe_subheader,recipeIngredie = [],[]
                    for recipesubheader in response_s.xpath('//div[@id="rcpinglist"]/h2/*'):
                        if 'recipe_subheader' in recipesubheader.xpath('./@class').extract():
                            if recipe_subheader != [] and recipeIngredie != []:
                                recipeIngredient_list.append(f"{recipe_subheader[0]} : {','.join(recipeIngredie)}")
                                recipe_subheader, recipeIngredie = [], []
                                recipe_subheader.append(recipesubheader.xpath('.//text()').extract_first())
                            else:
                                recipe_subheader.append(recipesubheader.xpath('.//text()').extract_first())
                        else:
                            recipeIngredient_selector = re.sub(' +',' ',''.join(recipesubheader.xpath('.//text()').extract()))
                            if recipeIngredient_selector != '':
                                recipeIngredie.append(recipeIngredient_selector)
                    recipeIngredient_list.append(f"{recipe_subheader[0]} : {','.join(recipeIngredie)}")
                    api_response['recipeIngredient'] = recipeIngredient_list
                except Exception as e:
                    print(e)
                    api_response['recipeIngredient'] = []
                try:
                    recipeInstructions = []
                    # recipeInst = response_s.xpath('//*[@itemprop="recipeInstructions"]')
                    for recipeInst in response_s.xpath('//*[@itemprop="recipeInstructions"]'):
                        instruction1 = recipeInst.xpath('.//span//text()').extract()
                        instruction = [s.strip() for s in instruction1]
                        inst_tmp = []
                        for inst in instruction:
                            instruction2 = re.sub(r'\n|\t|\r','',inst)
                            if instruction2 != ', ' and instruction2 != '':
                                inst_tmp.append(instruction2)
                        # if instruction2 != ', ' and instruction2 != '':
                        recipeInstructions.append(','.join(inst_tmp))
                    api_response['recipeInstructions'] = recipeInstructions
                except:api_response['recipeInstructions'] = []
                nutrition = {"@type":"NutritionInformation"}
                try:
                    nutrition_selectors = response_s.xpath('//*[@itemprop="nutrition"]/table//td[2]/span')
                    for nutrition_selector in nutrition_selectors:
                        n_key = nutrition_selector.xpath('./@itemprop').extract_first().strip()
                        n_value = nutrition_selector.xpath('./text()').extract_first().strip()
                        nutrition[n_key] = n_value
                    api_response['nutrition'] = nutrition
                except:api_response['nutrition'] = {}
            return api_response
        else:
            if response.status_code == 400:
                api_response = {"error": "(url) not found in request ..."}
            if response.status_code == 503:
                api_response = {"error": "Try after sometime"}
            if response.status_code == 503:
                api_response = {"error": "Try after sometime"}

    except Exception as e:
        print(e)


if __name__ == '__main__':
    urls = ['https://www.allrecipes.com/recipe/53729/fish-tacos/','https://www.angelwongskitchen.com/chinese-almond-cookie-recipe.html',
            'http://quietinthechaos.com/category/counter-culture/','https://heritagerecipes.blogspot.com/2013/03/large-layer-cake-instructions.html?m=1',
            'https://www.sbs.com.au/food/article/2021/07/20/japanese-comfort-dish-thats-also-viral-sensation','https://www.thebrewerandthebaker.com/archives/11487',
            'https://shanghaispice.wordpress.com/2015/04/22/brown-butter-black-currant-dark-chocolate-oatmeal-cookies/','http://picturetherecipe.com/recipe-videos/lemongrass-chicken-gyoza/',
            'https://www.paulhollywood.com/post/soda-bread']
    for url in urls:
        print(json.dumps(recipe_data(url)))
