import pandas as pd
from .models import projectOverview
file = "D:\\YaoLiang\\大三\\软件工程课设\\数据库及软件工程课程设计资料\\data.xlsx"
df_projectOverview = pd.read_excel(file, sheet_name="Sheet1")
df_siteProfile = pd.read_excel(file, sheet_name="Sheet2")
df_temperature = pd.read_excel(file, sheet_name="Sheet3")
list_projectOverview = []
for i in range(11):
    list_projectOverview.append(
        projectOverview(df_projectOverview['项目序号'][i],
                        df_projectOverview['项目名称'][i],
                        df_projectOverview['项目类型'][i],
                        df_projectOverview['项目阶段'][i],
                        df_projectOverview['项目业主'][i],
                        df_projectOverview['项目业主所属集团'][i],
                        df_projectOverview['设计单位'][i],
                        df_projectOverview['日期'][i]))
projectOverview.objects.bulk_create(list_projectOverview)
