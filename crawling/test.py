def crawl_images(query, path):

    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
         'v=1.0&q=' + query + '&start=%d'

    BASE_PATH = os.path.join(path, query)

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    counter = 1
    urls = []
    start = 0 # Google's start query string parameter for pagination.
    while start < 60: # Google will only return a max of 56 results.
        r = requests.get(BASE_URL % start)
        for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            print url
            urls.append(url)
            image = urllib.URLopener()

            try:
                image.retrieve(url,"model runway/image_"+str(counter)+".jpg")
                counter +=1
            except IOError, e:
                # Throw away some gifs...blegh.
                print 'could not save %s' % url
                continue

        print start
        start += 4 # 4 images per page.
        time.sleep(1.5)

crawl_images('model runway', '')
