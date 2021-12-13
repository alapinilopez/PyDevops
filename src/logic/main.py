from write_cars_all import *
from write_cars_lte import *
from write_cars_year import *
from hugo_run import *


write_cars_all_posts(md_cars)
write_cars_all_content(md_cars)

write_cars_lte_posts(md_cars_cheaper)
write_cars_lte_content(md_cars_cheaper)

write_cars_year_posts(md_cars_classics)
write_cars_year_content(md_cars_classics)

hugo_run()