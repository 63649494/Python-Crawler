from scrapy import cmdline
name='housespider -o douban.csv'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
