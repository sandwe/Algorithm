select fp.product_id, fp.product_name, sum(fp.price * fo.amount) as total_sales
from food_product fp
join food_order fo on fp.product_id = fo.product_id
where year(fo.produce_date) = '2022' and month(fo.produce_date) = '5'
group by fp.product_name
order by total_sales desc, fp.product_id