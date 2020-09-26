from django.db import models

# Create your models here.

class BusinessOrder(models.Model):
    # id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BILLNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billdate1 = models.CharField(db_column='BILLDATE1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billdate = models.CharField(db_column='BILLDATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yearmonth = models.CharField(db_column='YEARMONTH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    days = models.CharField(db_column='DAYS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentname = models.CharField(db_column='PARENTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shopcode = models.CharField(db_column='SHOPCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shopname = models.CharField(db_column='SHOPNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shopproperty = models.CharField(db_column='SHOPPROPERTY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    whareatypecode = models.CharField(db_column='WHAREATYPECODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodsid = models.CharField(db_column='GOODSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodscode = models.CharField(db_column='GOODSCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodsname = models.CharField(db_column='GOODSNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    singleproductid = models.CharField(db_column='SINGLEPRODUCTID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    singleproductcode = models.CharField(db_column='SINGLEPRODUCTCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    singleproductname = models.CharField(db_column='SINGLEPRODUCTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='WEIGHT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    laborcoststandard = models.CharField(db_column='LABORCOSTSTANDARD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    laborcostactual = models.CharField(db_column='LABORCOSTACTUAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='DISCOUNT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qty = models.CharField(db_column='QTY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=38, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountretail = models.CharField(db_column='AMOUNTRETAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amounttag = models.CharField(db_column='AMOUNTTAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualcost = models.CharField(db_column='ACTUALCOST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amountsettle = models.CharField(db_column='AMOUNTSETTLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amountverify = models.CharField(db_column='AMOUNTVERIFY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amountsharesettle = models.CharField(db_column='AMOUNTSHARESETTLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amountshare = models.CharField(db_column='AMOUNTSHARE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    couponsno = models.CharField(db_column='COUPONSNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    issettlement = models.CharField(db_column='ISSETTLEMENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discountrate = models.CharField(db_column='DISCOUNTRATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discounttype = models.CharField(db_column='DISCOUNTTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcebillno = models.CharField(db_column='SOURCEBILLNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vipcardno = models.CharField(db_column='VIPCARDNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderbilltype = models.CharField(db_column='ORDERBILLTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generaltype = models.CharField(db_column='GENERALTYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddremark = models.CharField(db_column='DDREMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderamount = models.CharField(db_column='ORDERAMOUNT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderqty = models.CharField(db_column='ORDERQTY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    holiday = models.CharField(db_column='HOLIDAY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classi = models.CharField(db_column='CLASSI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classii = models.CharField(db_column='CLASSII', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='PRODUCTNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Business_order'
    
class testSalesVolumn(models.Model):
    billdate = models.DateField(db_column='BILLDATE1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=38, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testSalesVolumn'
