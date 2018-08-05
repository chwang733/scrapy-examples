#execute spider and save the output to json line file
scrapy crawl sportsdirect-tshirt --set FEED_URI=products.jl

#To download images automatically. use image pipeline
1. add the following image pipeline to settings.py
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

2. For image pipeline to work, make sure to have image_urls and images to be defined in items.py 

3. execute spider and save the output 
scrapy crawl sportsdirect-tshirt --set FEED_URI=products.jl --set IMAGES_STORE=images  