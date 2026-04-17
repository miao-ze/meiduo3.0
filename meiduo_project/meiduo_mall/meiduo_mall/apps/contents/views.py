from django.shortcuts import render
from django.views import View
from meiduo_project.meiduo_mall.meiduo_mall.apps.goods.models import GoodsCategory,GoodsChannelGroup,GoodsChannel
from collections import OrderedDict


class IndexViews(View):
    def get(self,request):
        # # 查询商品分类数据
        # # 先准备一个大字典来装所有数据
        # # categories = {}           #（优化前1）
        # categories = OrderedDict()  #(优化后1)
        # # 为了方便后续的查找操作选择（商品频道）数据库来开始查找
        # # channels = GoodsChannel.objects.all()  #-->找到对应的37个频道，也就是一级类型   #(优化前2)
        # channels = GoodsChannel.objects.order_by('group_id','sequence')  #(优化后2)
        # for channel in channels:
        #     # 找到对应channel的频道组，即group_id（11个频道组）
        #     group_id = channel.group_id          #-->多查一（直接点出表里外键的字段名）
        #     # 因为频道组一共就11个，所以在进行添加数据时要进行判断
        #     if group_id not in categories:       #-->这样子就可以保证只有11个key
        #         categories[group_id] = {'channels':[],'sub_cats':[]}
        #     # 1.现在对channels中的数据进行构建
        #     cat1 = channel.category              #-->通过外键直接找到这个一级数据
        #     categories[group_id]['channels'].append({'id':cat1.id,'name':cat1.name,'url':channel.url})
        #
        #
        #     # 按视频方法来进行构造二级和三级数据
        #
        #
        #     # # 2.现在对sub_cats进行构建 (这个是自己写的)
        #     cat2_list = GoodsCategory.objects.filter(parent_id=cat1.id)
        #     for cat2 in cat2_list:
        #         # 先定义二级分类字典，持有三级分类的空列表
        #         cat2_item = {'id': cat2.id, 'name': cat2.name, 'sub_cats': []}
        #         categories[group_id]['sub_cats'].append(cat2_item)
        #
        #         # 构建三级分类，往当前二级分类的sub_cats里追加
        #         cat3_list = GoodsCategory.objects.filter(parent_id=cat2.id)
        #         for cat3 in cat3_list:
        #             cat2_item['sub_cats'].append({'id': cat3.id, 'name': cat3.name})
        #
        #
        # # 构造上下文数据
        # context = {
        #     'categories':categories
        # }
        return render(request,'index.html',context=context)