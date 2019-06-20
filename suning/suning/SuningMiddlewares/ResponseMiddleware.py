
class SuningResponseMiddleware(object):
    def process_response(self, request, response, spider):
        print('SuningResponseMiddleware process_response, request_url: %s, response_code: %s, spider: %s',request.url, response.status, spider.name)
        # ReptileUrlItem = {}
        # ReptileUrlItem['spider_name'] = spider.name
        # ReptileUrlItem['url'] = response.url
        # ReptileUrlItem['code'] = response.status
        # Add().insertReptile(ReptileUrlItem)
        return response