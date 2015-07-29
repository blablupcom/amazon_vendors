from amazon.api import AmazonAPI
import amazonproduct
import bottlenose
from bs4 import BeautifulSoup as bs


access_key = 'AKIAJ4A4R7O476HVZKKQ'
secret_key = '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'
associate_tag = 'safehavncom-20'
config = {
    'access_key': access_key,
    'secret_key': secret_key,
    'associate_tag': associate_tag,
    'locale': 'us'
    }
api = amazonproduct.API(cfg=config)
import bottlenose

a_title=''

amazon_tag = bottlenose.Amazon(access_key, secret_key, associate_tag)
tag = amazon_tag.ItemSearch(ItemId='020559526X',  ResponseGroup='Large', SearchIndex='All')
s = bs(tag)
print  s
# res = api.similarity_lookup('020559526X' , ResponseGroup='Large', Condition='All')
# print res
#
# for item in res.Items.Item:
#        try:
#           a_title = item.ItemAttributes.Title, item.ASIN
#       except: pass
#       print a_title