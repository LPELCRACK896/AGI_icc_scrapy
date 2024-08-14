from itemadapter import ItemAdapter
from icc_scraper.items import GroupItem, StationItem, VariableItem

class IccScraperPipeline:
    def process_item(self, item, spider):
        return item

