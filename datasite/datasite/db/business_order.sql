USE [CDPTEST]
GO
/****** Object:  Table [dbo].[Business_Order]    Script Date: 2020/6/6 14:11:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Business_Order](
	[ID] [varchar](50) NOT NULL,
	[BILLNO] [varchar](50) NULL,
	[BILLDATE1] [datetime2](7) NULL,
	[BILLDATE] [datetime2](7) NULL,
	[YEARMONTH] [varchar](50) NULL,
	[DAYS] [varchar](50) NULL,
	[PARENTNAME] [varchar](500) NULL,
	[NAME] [varchar](500) NULL,
	[SHOPCODE] [varchar](128) NULL,
	[SHOPNAME] [varchar](256) NULL,
	[SHOPPROPERTY] [varchar](50) NULL,
	[WHAREATYPECODE] [varchar](128) NULL,
	[STATUS] [varchar](50) NULL,
	[GOODSID] [int] NULL,
	[GOODSCODE] [varchar](128) NULL,
	[GOODSNAME] [varchar](500) NULL,
	[SINGLEPRODUCTID] [int] NULL,
	[SINGLEPRODUCTCODE] [varchar](128) NULL,
	[SINGLEPRODUCTNAME] [varchar](256) NULL,
	[WEIGHT] [numeric](12, 3) NULL,
	[LABORCOSTSTANDARD] [numeric](12, 2) NULL,
	[LABORCOSTACTUAL] [numeric](12, 2) NULL,
	[DISCOUNT] [numeric](12, 4) NULL,
	[QTY] [numeric](12, 4) NULL,
	[AMOUNT] [numeric](12, 4) NULL,
	[AMOUNTRETAIL] [numeric](12, 2) NULL,
	[AMOUNTTAG] [numeric](12, 4) NULL,
	[ACTUALCOST] [numeric](12, 2) NULL,
	[AMOUNTSETTLE] [numeric](12, 4) NULL,
	[AMOUNTVERIFY] [numeric](12, 4) NULL,
	[AMOUNTSHARESETTLE] [numeric](12, 4) NULL,
	[AMOUNTSHARE] [numeric](12, 4) NULL,
	[COUPONSNO] [varchar](1024) NULL,
	[ISSETTLEMENT] [varchar](50) NULL,
	[DISCOUNTRATE] [numeric](12, 4) NULL,
	[DISCOUNTTYPE] [varchar](386) NULL,
	[SOURCEBILLNO] [varchar](128) NULL,
	[REMARKS] [varchar](max) NULL,
	[VIPCARDNO] [varchar](50) NULL,
	[ORDERBILLTYPE] [varchar](50) NULL,
	[GENERALTYPE] [varchar](50) NULL,
	[DDREMARK] [varchar](255) NULL,
	[ORDERAMOUNT] [numeric](12, 4) NULL,
	[ORDERQTY] [numeric](12, 4) NULL,
	[TIMESTAMP] [datetime2](7) NULL,
	[BRAND] [varchar](10) NULL,
	[HOLIDAY] [nvarchar](30) NULL,
	[CLASSI] [nvarchar](256) NULL,
	[CLASSII] [nvarchar](256) NULL,
	[PRODUCTNAME] [nvarchar](256) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'订单总金额' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Business_Order', @level2type=N'COLUMN',@level2name=N'ORDERAMOUNT'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'订单总件数' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Business_Order', @level2type=N'COLUMN',@level2name=N'ORDERQTY'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'品牌' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Business_Order', @level2type=N'COLUMN',@level2name=N'BRAND'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'节日' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Business_Order', @level2type=N'COLUMN',@level2name=N'HOLIDAY'
GO
