import BH_ProductUOversion as UOM

# To be uncommented after the DM-QM integration
region = context.Quote.GetCustomField("Opportunity_Region").Value
if len(context.Quote.GetCustomField('Sub_Region').Value.split(' - ')) > 1:
    area = context.Quote.GetCustomField("Sub_Region").Value.split(' - ')[2]
else:
    area = ''
quoteCountry = context.Quote.GetCustomField('BH_Opportunity_Account_Country_quote').Value

# Hardcoding Area and region
'''context.Quote.GetCustomField("Area").Value = "Alaska"
context.Quote.GetCustomField("Region").Value = "North America"

region = context.Quote.GetCustomField("Region").Value
area = context.Quote.GetCustomField("Area").Value'''

for item in context.Items:
    Trace.Write('Floor Price GS UOM 1' + str(item['UOM']))
    item['List_Price'] = item.ListPrice
    item['BH_UserEnter_NetPrice'] = item.ListPrice
    item['LATAM_NetPrice_WithTax'] = item.ListPrice
    item['LATAM_Tax'] = 0
    if context.Product.FamilyCode == "CWI":
        item['CustProdDescription'] = str(item.DescriptionLong)
    if 'COPPER ADDER' in item.Description or 'LEAD ADDER' in item.Description:
        item['FloorPrice'] = item.ListPrice
        # item['UOM'] = SqlHelper.GetFirst("SELECT UnitOfMeasure FROM PRODUCTS WHERE PRODUCT_CATALOG_CODE = '" +  context.Product.PartNumber + "'").UnitOfMeasure
        if item["CreatedFromContract"] == "Yes":
            unitOfMeasure = item['UOM']
            Trace.Write('CreatedFromContract?' + str(item["CreatedFromContract"]))
            Trace.Write('unitOfMeasure?' + str(item["UOM"]))
            conversionFactor = UOM.productUOMConversion(str(unitOfMeasure), context)
            convContractPrice = item["Contract_Price"] * conversionFactor
            item["Contract_Price"] = convContractPrice
        else:
            unitOfMeasure = SqlHelper.GetFirst(
                "SELECT UnitOfMeasure FROM PRODUCTS WHERE PRODUCT_CATALOG_CODE = '" + context.Product.PartNumber + "'").UnitOfMeasure
            item['UOM'] = unitOfMeasure
        if context.Quote.GetCustomField('BH_UOM_System').Value == 'IMPERIAL':
            if unitOfMeasure != '':
                if unitOfMeasure == 'M':
                    item['UOM'] = 'FT'
                if unitOfMeasure == 'L':
                    item['UOM'] = 'GAL'
                if unitOfMeasure == 'KM':
                    item['UOM'] = 'MI'
                if unitOfMeasure == 'KG':
                    item['UOM'] = 'LB'
        if context.Quote.GetCustomField('BH_UOM_System').Value == 'METRIC':
            if unitOfMeasure != '':
                if unitOfMeasure == 'FT':
                    item['UOM'] = 'M'
                if unitOfMeasure == 'GAL':
                    item['UOM'] = 'L'
                if unitOfMeasure == 'MI':
                    item['UOM'] = 'KM'
                if unitOfMeasure == 'LB':
                    item['UOM'] = 'KG'
    else:
        if context.Product.Attributes.GetByName('Copper Adder') is not None:
            item['CuAdderApproval'] = 'No'
            if context.Product.Attributes.GetByName('Copper Adder').GetValue() == '':
                item['CuAdderApproval'] = 'Yes'
        productFamily = context.Product.FamilyCode
        productRevenueType = context.Product.Type.Name
        # item['UOM'] = SqlHelper.GetFirst("SELECT UnitOfMeasure FROM PRODUCTS WHERE PRODUCT_CATALOG_CODE = '" +  context.Product.PartNumber + "'").UnitOfMeasure
        if item["CreatedFromContract"] == "Yes":
            unitOfMeasure = item['UOM']
            Trace.Write('CreatedFromContract?' + str(item["CreatedFromContract"]))
            Trace.Write('unitOfMeasure?' + str(item["UOM"]))
            conversionFactor = UOM.productUOMConversion(str(unitOfMeasure), context)
            convContractPrice = item["Contract_Price"] * conversionFactor
            item["Contract_Price"] = convContractPrice
        else:
            unitOfMeasure = SqlHelper.GetFirst(
                "SELECT UnitOfMeasure FROM PRODUCTS WHERE PRODUCT_CATALOG_CODE = '" + context.Product.PartNumber + "'").UnitOfMeasure
            item['UOM'] = unitOfMeasure
        if context.Quote.GetCustomField('BH_UOM_System').Value == 'IMPERIAL':
            if unitOfMeasure != '':
                if unitOfMeasure == 'M':
                    item['UOM'] = 'FT'
                if unitOfMeasure == 'L':
                    item['UOM'] = 'GAL'
                if unitOfMeasure == 'KM':
                    item['UOM'] = 'MI'
                if unitOfMeasure == 'KG':
                    item['UOM'] = 'LB'
        if context.Quote.GetCustomField('BH_UOM_System').Value == 'METRIC':
            if unitOfMeasure != '':
                if unitOfMeasure == 'FT':
                    item['UOM'] = 'M'
                if unitOfMeasure == 'GAL':
                    item['UOM'] = 'L'
                if unitOfMeasure == 'MI':
                    item['UOM'] = 'KM'
                if unitOfMeasure == 'LB':
                    item['UOM'] = 'KG'
        Trace.Write('Floor Price GS UOM 2' + str(item['UOM']))
        item['Engineering_Part_Number'] = SqlHelper.GetFirst(
            "SELECT MPN FROM PRODUCTS WHERE PRODUCT_CATALOG_CODE = '" + context.Product.PartNumber + "'").MPN
        if productFamily == "DB":
            item['BitType'] = ''
            item['BitSize'] = ''
            BrandingProductName = ''
            if context.Product.Attributes.GetByName('Bit Type') is not None:
                item['BitType'] = context.Product.Attributes.GetByName('Bit Type').GetValue()
            if context.Product.Attributes.GetByName('Bit Diameter') is not None:
                item['BitSize'] = context.Product.Attributes.GetByName('Bit Diameter').GetValue()
            if context.Product.Attributes.GetByName('Branding Product Name') is not None:
                BrandingProductName = context.Product.Attributes.GetByName('Branding Product Name').GetValue()
            discountThresholdQuery = "SELECT DISCOUNT_THRESHOLD FROM DB_DISCOUNT_TABLE_FLOOR_PRICE_CALCULATION WHERE REVENUE_TYPE = '" + str(
                item.ProductTypeName) + "' AND REGION = '{0}' AND AREA = '{1}' AND BIT_TYPE = '{2}' AND PRODUCT_NAME = '{3}'".format(
                region, area, item['BitType'], BrandingProductName)
            Trace.Write("FPC DISCOUNT QUERY : " + discountThresholdQuery)
            discountThreshold = SqlHelper.GetFirst(discountThresholdQuery)
            if discountThreshold is not None:
                Trace.Write("FPC DISCOUNT THRESHOLD : " + str(discountThreshold.DISCOUNT_THRESHOLD))
                item['FloorPrice'] = str((item.ListPrice) * (1 - float(discountThreshold.DISCOUNT_THRESHOLD)))
                item['BH_FloorPrice_Orig'] = str((item.ListPrice) * (1 - float(discountThreshold.DISCOUNT_THRESHOLD)))
        else:
            Trace.Write('Eles side of script: item.CategoryId=' + str(item.CategoryId))
            category_Id = ''
            al = SqlHelper.GetFirst("select * from PRODUCTS where PRODUCT_CATALOG_CODE= '" + str(item.PartNumber) + "'")
            if al is not None:
                directory_cd = SqlHelper.GetFirst(
                    "select * from Directory where product_id='" + str(al.PRODUCT_ID) + "'")
                if directory_cd is not None:
                    category_Id = str(directory_cd.DIRECTORY_CD)
            #			if item.CategoryId != 0:
            #				category_Id = str(item.CategoryId)
            getCategoryName = SqlHelper.GetFirst("SELECT * FROM DIRECTORY_DEFN WHERE DIRECTORY_CD = " + category_Id)
            if getCategoryName is not None:
                if productFamily == "ALS":
                    if region.upper() == "North America".upper():
                        discountThresholdQuery = "SELECT DISCOUNT_THRESHOLD FROM ALS_DISCOUNT_TABLE_FLOOR_PRICE_CALCULATION WHERE REVENUE_TYPE = '" + str(
                            item.ProductTypeName) + "'AND PRODUCT_FAMILY = '" + str(
                            getCategoryName.DIR_NAME) + "' AND AREA = '{0}'".format(area)
                    else:
                        discountThresholdQuery = "SELECT DISCOUNT_THRESHOLD FROM ALS_DISCOUNT_TABLE_FLOOR_PRICE_CALCULATION WHERE REVENUE_TYPE = '" + str(
                            item.ProductTypeName) + "'AND PRODUCT_FAMILY = '" + str(
                            getCategoryName.DIR_NAME) + "' AND COUNTRY = '{0}'".format(quoteCountry)
                if productFamily == "OIC":
                    discountThresholdQuery = "SELECT * FROM OIC_FLOOR_PRICE WHERE MATERIAL_NUMBER ='" + str(
                        item.PartNumber) + "' AND PRODUCT_TYPE = '" + str(
                        item.ProductTypeName) + "' AND AREA = '{0}'".format(area)
                if productFamily == "CWI":
                    if context.Product.Attributes.GetByName('CWI Sub Product Line') is not None:
                        item['SubProductLine'] = context.Product.Attributes.GetByName('CWI Sub Product Line').GetValue()
                    if context.Product.Attributes.GetByName('CWI Product Family') is not None:
                        item['Category_Name'] = context.Product.Attributes.GetByName('CWI Product Family').GetValue()
                    # item['Category_Name'] = context.Product.Attributes.GetByName('CWI Product Family').SelectedValue.ValueCode
                    if context.Product.Attributes.GetByName('CWI Pricing Cond Type') is not None:
                        item['PricingConditionType'] = context.Product.Attributes.GetByName(
                            'CWI Pricing Cond Type').SelectedValue.ValueCode
                        item['BH_PricingCondTypeDesc'] = context.Product.Attributes.GetByName(
                            'CWI Pricing Cond Type').GetValue()
                    discountThresholdQuery = "SELECT DISCOUNT_THRESHOLD FROM CWI_DISC_TABLE_FLOOR_PRICE_CALC WHERE REVENUE_TYPE = '" + str(
                        item.ProductTypeName) + "'AND PROD_FAMILY = '" + str(
                        item['Category_Name']) + "' AND AREA = '{0}'".format(area)
                Trace.Write("FPC DISCOUNT QUERY : " + discountThresholdQuery)
                discountThreshold = SqlHelper.GetFirst(discountThresholdQuery)
                if discountThreshold is not None:
                    # Trace.Write("FPC DISCOUNT THRESHOLD : " + str(discountThreshold.DISCOUNT_THRESHOLD))
                    if productFamily == "OIC":
                        calculatedFloorPrice = str(discountThreshold.FLOOR_PRICE)
                    else:
                        calculatedFloorPrice = (item.ListPrice) * (1 - float(discountThreshold.DISCOUNT_THRESHOLD))
                    item['FloorPrice'] = str(calculatedFloorPrice)
                    item['BH_FloorPrice_Orig'] = str(calculatedFloorPrice)
