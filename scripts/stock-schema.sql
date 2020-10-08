-- ------------------------------------------------------
-- PostgreSQL Version 12
-- Host: 127.0.0.1    
-- Database Name: stock
-- version: 1.0
-- create time: 20200709
-- modify time: 20200713
-- 说明：生命线股票研究
-- ------------------------------------------------------

--
-- postgresql 创建库表
DROP DATABASE IF EXISTS stock;
create user racher with password '123.com';
create database stock owner racher encoding 'UTF8';


drop table stock_partner;

create table focus_stock (
create_time  timestamp(0) without time zone not null ,
sk_symbol smallint NOT NULL,
base_data json,
partner_info json
);

comment on table focus_stock is '重点关注股票';
comment on column focus_stock.create_time is '抓取数据时间，即股票数据入库时间';
comment on column focus_stock.sk_symbol is '股票代码。例子，000001 为上证指数';
comment on column focus_stock.partner_info is '股东信息。包括：公告日期、 股东名称、 持股数量（股）、 占流通股比例(%)、 股本性质';
alter table "focus_stock" alter column sk_symbol type integer;
alter table "focus_stock" alter sk_symbol type int using sk_symbol::integer;

# \l 查看数据库
# \d 查看数据表

# \dtS+ focus_stock;查看表注释信息
# \dS+ focus_stock;查看表字段注释信息


--贵州茅台
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"中国贵州茅台酒厂(集团)有限责任公司","sk_amount":728531955,"sk_percentage":57.995,"sk_attribute":"国有股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"香港中央结算有限公司","sk_amount":106148171,"sk_percentage":8.450,"sk_attribute":"境外法人股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"贵州省国有资本运营有限责任公司","sk_amount":50240000,"sk_percentage":3.999,"sk_attribute":"国有股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"贵州茅台酒厂集团技术开发公司","sk_amount":27812088,"sk_percentage":2.214,"sk_attribute":"国有股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"中央汇金资产管理有限责任公司","sk_amount":10787300,"sk_percentage":0.859,"sk_attribute":"国有股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"中国证券金融股份有限公司","sk_amount":8039538,"sk_percentage":0.640,"sk_attribute":"国有股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"深圳市金汇荣盛财富管理有限公司－金汇荣盛三号私募证券投资基金","sk_amount":5020950,"sk_percentage":0.400,"sk_attribute":"境内法人股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"珠海市瑞丰汇邦资产管理有限公司－瑞丰汇邦三号私募证券投资基金","sk_amount":4095932,"sk_percentage":0.326,"sk_attribute":"境内法人股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"中国人寿保险股份有限公司－传统－普通保险产品－005L－CT001沪","sk_amount":3845138,"sk_percentage":0.306,"sk_attribute":"境内法人股"}');
insert into focus_stock (create_time, sk_symbol, partner_info) values ('2020-10-05 16:46:03', '600519', '{"sk_time":"2020-06-30","sk_name":"贵州金融控股集团有限责任公司(贵州贵民投资集团有限责任公司)","sk_amount":3487220,"sk_percentage":0.278,"sk_attribute":"国有股"}');


--查询语句总结

select row_to_json(focus_stock) from focus_stock;
select row_to_json(row("sk_symbol","partner_info")) from focus_stock;
select partner_info ->> 'sk_time' as 公告时间, partner_info ->>'sk_name' as 股东名称  from focus_stock where sk_symbol = 'sz00
0063';
select partner_info ->> 'sk_time' as 公告时间, partner_info ->>'sk_name' as 股东名称  from focus_stock where sk_symbol = 'sz00
0063' and partner_info ->>'sk_name' = '中兴新通讯有限公司';
 select sk_symbol as 股票代码, partner_info ->> 'sk_time' as 公告时间, partner_info ->>'sk_name' as 股东名称  from focus_stock w
here partner_info ->>'sk_name' = '香港中央结算有限公司';

select sk_symbol as 股票代码,partner_info ->> 'sk_time' as 公告时间, partner_info ->>'sk_name' as 股东名称, partner_info ->>'s
k_amount' as 持股数（股）  from focus_stock where partner_info ->>'sk_amount' > '752339100';

select sk_symbol as 股票代码, partner_info ->> 'sk_name' as 股东名称 from focus_stock;

select * from focus_stock where sk_symbol = (select sk_symbol from stock_pool where sk_name = '浦发银行');


DELETE from focus_stock where sk_symbol = 600519;
select current_timestamp;

select f.sk_symbol as 股票代码, p.sk_name as 股票名称, partner_info ->> 'sk_name' as 股东名称 from focus_stock f , stock_pool p where p.sk_symbol = f.sk_sym
bol;

select sk_symbol,count(sk_symbol) from focus_stock GROUP BY sk_symbol;

--查询focus_stock 表没有股东数据的股票
select * from stock_pool where sk_symbol not in (select sk_symbol from focus_stock where sk_symbol is not null);
--
-- 创建股票代码池
--
drop table stokc_pool;


create table stokc_pool (
sk_symbol integer NOT NULL,
sk_name varchar(8) not null
);

comment on table stokc_pool is '基础股票池';
comment on column stokc_pool.sk_symbol is '股票代码。例子，002315';
comment on column stokc_pool.sk_name is '股票名称。例子，焦点科技';

alter table stokc_pool rename sk_symbol to sk_number;
alter table stokc_pool rename to stock_pool;

--插入创业板股票
insert into stokc_pool values(300001, '特锐德');

delete from stokc_pool where sk_symbol = '300295';
--
-- 创建股票交易信息表
--

create table if not exists stock_business(
    sk_date date comment '交易日期',
    sk_symbol varchar(8) comment '股票代码',
    sk_name varchar(20) comment '股票名称',
    sk_open float(5,2) comment '开盘价',
    sk_close float(5,2) comment '收盘价',
    sk_high float(5,2) comment '最高价',
    sk_low float(5,2) comment '最低价',
    sk_preclose float(5,2) comment '前天收盘价',
    sk_vol float(5,2) comment '成交量',
    sk_amount float(5,2) comment '成交额',
    sk_pct_chg float(5,2) comment '涨跌幅',
    sk_vol_ratio float(5,2) comment '量比',
    sk_adjustflag int comment '复权状态',
    sk_trun float(5,2) comment '换手率',
    sk_tradestatus int comment '交易状态',
    sk_pctChg float(5,2) comment '涨跌幅',
    sk_peTTM float(5,2) comment '滚动市盈率',
    sk_pbMRQ float(5,2) comment '市净率',
    sk_psTTM float(5,2) comment '滚动市销率',
    sk_pcfNcfTTM float(5,2) comment '滚动市现率',
    sk_isST int comment '是否ST股'
) comment = '股票交易信息';
