#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-05 01:14:19
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba

# url = ['soueast.i.auto.sohu.com', 'dodge.i.auto.sohu.com', 'gol.i.auto.sohu.com', 'linyi.auto.sohu.com', 'hexie.i.auto.sohu.com', 'wuhan.auto.sohu.com', 'fengyun.i.auto.sohu.com', 'lancerevo.i.auto.sohu.com', 'ad.sh.sohu.com', 'club.women.sohu.com', 'maybach.i.auto.sohu.com', 'pic.2008.sohu.com', 'changsha.auto.sohu.com', 'mgmg6.i.auto.sohu.com', 'regal.i.auto.sohu.com', 'hljcyh.i.auto.sohu.com', 'vela.i.auto.sohu.com', 'q.fund.sohu.com', 'sccyh.i.auto.sohu.com', 'qianlima.i.auto.sohu.com', 'bmw-z8.i.auto.sohu.com', 'app.tv.sohu.com', 'hhxy.i.auto.sohu.com', 'prius.i.auto.sohu.com', 'hengshui.i.auto.sohu.com', 'handan.auto.sohu.com', 'goabroad.sohu.com', 'mini.i.auto.sohu.com', 'nbcs.i.auto.sohu.com', 'yaku.i.auto.sohu.com', 'anhuifuwu.i.auto.sohu.com', 'golf.i.auto.sohu.com', 'haima.i.auto.sohu.com', 'a3.i.auto.sohu.com', 'karry.i.auto.sohu.com', 'ayham.i.auto.sohu.com', 'benteng.i.auto.sohu.com', 'club.stock.sohu.com', 'boxster.i.auto.sohu.com', 'bj.learning.sohu.com', 'hlgcyh.i.auto.sohu.com', 'lova.i.auto.sohu.com', 't.auto.sohu.com', 'chwang.i.auto.sohu.com', 'bentley.i.auto.sohu.com', 'zhuanti.club.it.sohu.com', 'mazida323.i.auto.sohu.com', 'sx4.i.auto.sohu.com', 'a4.i.auto.sohu.com', 'card.money.sohu.com', 'nmgcyh.i.auto.sohu.com', 'kunming.saa.auto.sohu.com', 'fengshens30.i.auto.sohu.com', 'jingqu.travel.sohu.com', '05133.astro.women.sohu.com', 'range-rover.i.auto.sohu.com', 'crown.i.auto.sohu.com', 'x-trail.i.auto.sohu.com', 'hbcyh.i.auto.sohu.com', 'mingshi.i.auto.sohu.com', 'zhuanti.club.auto.sohu.com', 'delica.i.auto.sohu.com', 'adidas.sports.sohu.com', 'lz.club.travel.sohu.com', 'corolla.i.auto.sohu.com', 'laguna.i.auto.sohu.com', 'jncyh.i.auto.sohu.com', 'previa.i.auto.sohu.com', 'f1.sports.sohu.com', 'jlcyh.i.auto.sohu.com', 'dfzzcross.i.auto.sohu.com', 'lingyuev3.i.auto.sohu.com', 'premacy.i.auto.sohu.com', 'bzzyh.i.auto.sohu.com', 'cbadata.sports.sohu.com', 'infiniti-fx.i.auto.sohu.com', 'landwind-x9.i.auto.sohu.com', 'chongqing.auto.sohu.com', 'commander.i.auto.sohu.com', 'qhdcy.i.auto.sohu.com', 'haixun.i.auto.sohu.com', 'gl8.i.auto.sohu.com', 'binyue.i.auto.sohu.com', 'yunnan.i.auto.sohu.com', 'legacy.i.auto.sohu.com', 'linzhou.i.auto.sohu.com', 'cangzhou.auto.sohu.com', 'sandafe.i.auto.sohu.com', 'lifan.i.auto.sohu.com', 'sip1040.i.auto.sohu.com', 'cangzhou.i.auto.sohu.com', 'club.cul.sohu.com', 'fengxing.i.auto.sohu.com', 'index.auto.sohu.com', 'rx-8.i.auto.sohu.com', 'toyota.i.auto.sohu.com', 'junjie.i.auto.sohu.com', 'club.comment2.news.sohu.com', 'saa.auto.sohu.com', 'lexusle.i.auto.sohu.com', 'saifu.i.auto.sohu.com', 'xn.xy.club.sohu.com', 'jiaxing.auto.sohu.com', 'mycarclub.i.auto.sohu.com', 'jinying.i.auto.sohu.com', 'p.club.women.sohu.com', 'kia.i.auto.sohu.com', 'yuexiang.i.auto.sohu.com', 'club.men.sohu.com', 'huapu.i.auto.sohu.com', 'pic.tv.sohu.com', 'product.news.sohu.com', 'tiidash.i.auto.sohu.com', 'sip2248.i.auto.sohu.com', 'caddy.i.auto.sohu.com', 'pic.news.sohu.com', 'pic.gongyi.sohu.com', 'volvos40.i.auto.sohu.com', 'lz.astro.sohu.com', 'weiqi.sports.sohu.com', 'sip1152.i.auto.sohu.com', 'mgf.i.auto.sohu.com', 'saddle.i.auto.sohu.com', 'huodong.i.auto.sohu.com', 'shxcy.i.auto.sohu.com', 'hebcyh.i.auto.sohu.com', 'sonatanfc.i.auto.sohu.com', 'bydf0.i.auto.sohu.com', 'smart.i.auto.sohu.com', 'sip2171.i.auto.sohu.com', 'baodian.women.sohu.com', 'riich.i.auto.sohu.com', 'dihao.i.auto.sohu.com', 'p.club.city.travel.sohu.com', 'chengdu.auto.sohu.com', 'zhuanti.club.business.sohu.com', 'bmw.i.auto.sohu.com', 'paladin.i.auto.sohu.com', 'club.yule.sohu.com', 'babyclub.women.sohu.com', 'pic.learning.sohu.com', 'lobo.i.auto.sohu.com', 'data.yule.sohu.com', 'shuanghuan.i.auto.sohu.com', 'tuangouauto.i.auto.sohu.com', 'mazadaruiyi.i.auto.sohu.com', 'gz.learning.sohu.com', 'camry2.i.auto.sohu.com', 'sportage.i.auto.sohu.com', 'club.city.women.sohu.com', 'picasso.i.auto.sohu.com', 'fund.sohu.com', 'boss.sports.sohu.com', 'jaguar-xk.i.auto.sohu.com', 'bmw-x3.i.auto.sohu.com', 'outdoor.travel.sohu.com', 'audia6.i.auto.sohu.com', 'lexusls.i.auto.sohu.com', 'goche.auto.sohu.com', 'whcyh.i.auto.sohu.com', 'bmw5.i.auto.sohu.com', 'guangzhou.auto.sohu.com', 'mazda32.i.auto.sohu.com', 'rodius.i.auto.sohu.com', 'cl.i.auto.sohu.com', 'haifuxing.i.auto.sohu.com', 'chihe.sohu.com', 'helper.i.auto.sohu.com', 'club.sh.sohu.com', 'book.sohu.com', 'discovery.i.auto.sohu.com', 'open.tv.sohu.com', 'lavida.i.auto.sohu.com', 'fengtai.i.auto.sohu.com', 'nanchang.auto.sohu.com', 'a2.i.auto.sohu.com', 'autosup0311.i.auto.sohu.com', 'bmw-z4.i.auto.sohu.com', 'prado.i.auto.sohu.com', 'mdx.i.auto.sohu.com', 'grandis.i.auto.sohu.com', 'zbllz.i.auto.sohu.com', 'dm.sohu.com', 'sdtiida.i.auto.sohu.com', 'ford-s-max.i.auto.sohu.com', 'pic.dm.sohu.com', '2008.sohu.com', 'q7.i.auto.sohu.com', 'vip.club.sohu.com', 'zhjcy.i.auto.sohu.com', 'lupo.i.auto.sohu.com', 'jinbei.i.auto.sohu.com', 'haodf.health.sohu.com', 'saima.i.auto.sohu.com', 'hzcyh.i.auto.sohu.com', 'tscyh.i.auto.sohu.com', 'beetle.i.auto.sohu.com', 'lingyang.i.auto.sohu.com', 'livina.i.auto.sohu.com', '17173.tv.sohu.com', 'wenzhou.auto.sohu.com', 'dwcyh.i.auto.sohu.com', 'slk-class.i.auto.sohu.com', 'gd.sohu.com', 'p.club.gd.sohu.com', 'echo.i.auto.sohu.com', 'p.club.business.sohu.com', 'i30.i.auto.sohu.com', 'carens.i.auto.sohu.com', 'allroad.i.auto.sohu.com', 'beijing.auto.sohu.com', '2004.sports.sohu.com', 'lamborghini.i.auto.sohu.com', 'xinan.i.auto.sohu.com', 'fudi.i.auto.sohu.com', 'crosspolo.i.auto.sohu.com', 'b50.i.auto.sohu.com', 'sail.i.auto.sohu.com', 'zhixiang.i.auto.sohu.com', 'pic.men.sohu.com', 'tiida-yida.i.auto.sohu.com', 'zhdcar.i.auto.sohu.com', 'jaguar-xj.i.auto.sohu.com', 'ccrhy.i.auto.sohu.com', 'wzcyh.i.auto.sohu.com', 'baobao.sohu.com', 'rx-7.i.auto.sohu.com', 'rollsroyce.i.auto.sohu.com', 'club.campus.sohu.com', 'banzhu.i.auto.sohu.com', 'youxi.sports.sohu.com', 'honda.i.auto.sohu.com', 'info.2012.sohu.com', 'db.i.auto.sohu.com', 'porsche.i.auto.sohu.com', 'roewe750.i.auto.sohu.com', 'shijixing.i.auto.sohu.com', 'borahb.i.auto.sohu.com', 'shxicyh.i.auto.sohu.com', 'kubao.i.auto.sohu.com', 'tianjin.auto.sohu.com', 'wlmqcyh.i.auto.sohu.com', '1soccer.sports.sohu.com', 'v.tv.sohu.com', 'volkswagen.i.auto.sohu.com', 'app.sh.sohu.com', 'hbbd.i.auto.sohu.com', 'yunque.i.auto.sohu.com', 'app.auto.sohu.com', 'nanjing.auto.sohu.com', 'pic.yule.sohu.com', 'aveo.i.auto.sohu.com', 'hongqi18.i.auto.sohu.com', 'sycyh.i.auto.sohu.com', 'lifan620.i.auto.sohu.com', 'heyue.i.auto.sohu.com', 'aveo2.i.auto.sohu.com', 'benz.i.auto.sohu.com', 'db.money.sohu.com', 'navigator.i.auto.sohu.com', 'myway.astro.women.sohu.com', 'epica.i.auto.sohu.com', 'sip2238.i.auto.sohu.com', 'alto.i.auto.sohu.com', 'cts.i.auto.sohu.com', 'xbxfz.i.auto.sohu.com', 'b-class.i.auto.sohu.com', 'daxue.learning.sohu.com', 'grand-vitara.i.auto.sohu.com', 'viano.i.auto.sohu.com', 'grandcherokee.i.auto.sohu.com', 'maserati.i.auto.sohu.com', 'xn.xy.learning.club.sohu.com', 'zhuanti.club.sports.sohu.com', 'qashqai.i.auto.sohu.com', 'lexusgs.i.auto.sohu.com', 'club.health.sohu.com', 'sdsail.i.auto.sohu.com', 'women.sohu.com', 'kizashi1.i.auto.sohu.com', 'money.business.sohu.com', 'lz.club.news.sohu.com', 'aygo.i.auto.sohu.com', 'try.women.sohu.com', 'buick.i.auto.sohu.com', 'xy.learning.club.sohu.com', 'zhongyi.i.auto.sohu.com', 'csldata.sports.sohu.com', 'text.news.sohu.com', 'mg.i.auto.sohu.com', 'elantra.i.auto.sohu.com', 's4.i.auto.sohu.com', 'tycyh.i.auto.sohu.com', 'tzzl.i.auto.sohu.com', 'smartfortwo.i.auto.sohu.com', 'adflash.sh.sohu.com', 'wuxi.auto.sohu.com', 's3.i.auto.sohu.com', 'cayenne.i.auto.sohu.com', 'haishi1.i.auto.sohu.com', 'zone.it.sohu.com', 'tpms.i.auto.sohu.com', 'data.sports.sohu.com', 'aichejiangtu.i.auto.sohu.com', 'yantai.auto.sohu.com', 'mitsubishi.i.auto.sohu.com', 'infiniti-g.i.auto.sohu.com', 'fit.i.auto.sohu.com', 'dise.health.sohu.com', 'vip.book.sohu.com', 'qiyun.i.auto.sohu.com', 'hyundai.i.auto.sohu.com', 'rs6.i.auto.sohu.com', 'neirong.i.auto.sohu.com', 'bdyuexiang.i.auto.sohu.com', 'game.tv.sohu.com', 'fulaier.i.auto.sohu.com', 'riichg5.i.auto.sohu.com', 'zhuanti.club.astro.sohu.com', 'jingxuan.i.auto.sohu.com', 'sharan.i.auto.sohu.com', 'transit.i.auto.sohu.com', 'hldcyh.i.auto.sohu.com', 'shxcyh.i.auto.sohu.com', 'sdcy.i.auto.sohu.com', 'gzcyh.i.auto.sohu.com', 'xialin3.i.auto.sohu.com', 'megane.i.auto.sohu.com', 'm.tv.sohu.com', 'game.2010.sohu.com', 'xianghe.i.auto.sohu.com', 'club.money.business.sohu.com', 'liberty.i.auto.sohu.com', 'tribeca.i.auto.sohu.com', 'business.sohu.com', 'mg3.i.auto.sohu.com', 'huhehaote.auto.sohu.com', 'clk-class.i.auto.sohu.com', 'bja5.i.auto.sohu.com', 'activity.i.auto.sohu.com', 'learning.sohu.com', 'arts.cul.sohu.com', 'changfeng.i.auto.sohu.com', 'sddz.i.auto.sohu.com', 'club.baobao.sohu.com', 'jingang.i.auto.sohu.com', 'huandong.i.auto.sohu.com', 'dalian.auto.sohu.com', 'suzuki.i.auto.sohu.com', 'handan.i.auto.sohu.com', 'bschool.sohu.com', 'jili.i.auto.sohu.com', 'sh.xy.club.sohu.com', 'focus.i.auto.sohu.com', 'lancer.i.auto.sohu.com', 'media.sohu.com',
#        'opel.i.auto.sohu.com', 'ziyoujian.i.auto.sohu.com', 'tuan.sohu.com', 'soccer.sports.sohu.com', 'data.2010.sohu.com', 'henancy.i.auto.sohu.com', 'money.sohu.com', 'huodongauto.i.auto.sohu.com', 'club.news.sohu.com', 'xsara.i.auto.sohu.com', 'changchun.auto.sohu.com', 'bmw-z3.i.auto.sohu.com', 'apple1218.i.auto.sohu.com', 'maverick.i.auto.sohu.com', 'life.women.sohu.com', 'sh.sohu.com', 'optima.i.auto.sohu.com', 'green.sohu.com', 'lexuslx.i.auto.sohu.com', 'e-class2.i.auto.sohu.com', 'zhuanti.club.yule.sohu.com', 'bjoulande.i.auto.sohu.com', 'jinan.auto.sohu.com', 'buy.auto.sohu.com', 'p.club.travel.sohu.com', 'tanglin7619.i.auto.sohu.com', '206.i.auto.sohu.com', 'sdst.i.auto.sohu.com', 'shcy.i.auto.sohu.com', 'book.news.sohu.com', 'bls.i.auto.sohu.com', 'zhuanti.club.learning.sohu.com', 'xiali.i.auto.sohu.com', 'jinan.i.auto.sohu.com', 'lancerex.i.auto.sohu.com', 'ningbo.auto.sohu.com', 'sorento.i.auto.sohu.com', 'chery-a3.i.auto.sohu.com', 'product.it.sohu.com', 'sheying.club.sohu.com', 'rohens.i.auto.sohu.com', 'bmw3.i.auto.sohu.com', 'sheny.tv.sohu.com', 'hefei.auto.sohu.com', 'grand-cherokee.i.auto.sohu.com', 'q.stock.sohu.com', 'astra.i.auto.sohu.com', 'lz.travel.sohu.com', 'p.club.sports.sohu.com', 'city.i.auto.sohu.com', 'galant.i.auto.sohu.com', 'mazda3s.i.auto.sohu.com', 'njcyh.i.auto.sohu.com', 'langfang.i.auto.sohu.com', 'qq6.i.auto.sohu.com', 'index.tv.sohu.com', 'c1.i.auto.sohu.com', 'acuratl.i.auto.sohu.com', 'freelander.i.auto.sohu.com', 'hongqi.i.auto.sohu.com', 'saab.i.auto.sohu.com', 'fiat.i.auto.sohu.com', 'hangzhou.auto.sohu.com', 'roll.sohu.com', 'pic.health.sohu.com', 's-type.i.auto.sohu.com', 'palioweekend.i.auto.sohu.com', 'club.goabroad.sohu.com', 'beta.club.sohu.com', 'zhuanti.club.chihe.sohu.com', 'hubeicy.i.auto.sohu.com', 'yueyue.i.auto.sohu.com', 'club.it.sohu.com', 'index.health.sohu.com', 'rqcyh.i.auto.sohu.com', 'heijingang.i.auto.sohu.com', 'lacrosse.i.auto.sohu.com', 'tjcy.i.auto.sohu.com', 'club.sports.sohu.com', 'bmw7.i.auto.sohu.com', 'camry.i.auto.sohu.com', 'lz.club.cul.sohu.com', 'tjky.i.auto.sohu.com', 'dealer.auto.sohu.com', 'pic.green.sohu.com', 'gtr.i.auto.sohu.com', 'tjcyh.i.auto.sohu.com', 'pic.money.sohu.com', 'accent.i.auto.sohu.com', 'xjcyh.i.auto.sohu.com', 'pic.it.sohu.com', 'mudanjiang.i.auto.sohu.com', 'media.news.sohu.com', 'ccsuteng.i.auto.sohu.com', 'p.club.health.sohu.com', 'park-avenue.i.auto.sohu.com', 'pajero.i.auto.sohu.com', 'xacyh.i.auto.sohu.com', 'landrover.i.auto.sohu.com', 'srx.i.auto.sohu.com', 'vision.i.auto.sohu.com', 'cccyh.i.auto.sohu.com', 'nr.book.sohu.com', 'weather.news.sohu.com', 'suzhou.auto.sohu.com', 'tt.i.auto.sohu.com', 'feiteng.i.auto.sohu.com', 'xinjunwei.i.auto.sohu.com', 'haimas1.i.auto.sohu.com', 'baoding.auto.sohu.com', 'cheyinghui.i.auto.sohu.com', 'fenghua.i.auto.sohu.com', 'go108.astro.women.sohu.com', 'wrangler.i.auto.sohu.com', 'scenic.i.auto.sohu.com', 'act.it.sohu.com', 'club.astro.sohu.com', 'games.sohu.com', 'dongfangzhizi.i.auto.sohu.com', 'opirus.i.auto.sohu.com', 's.sohu.com', 'neiguan.i.auto.sohu.com', 'data.tv.sohu.com', 'mazda6.i.auto.sohu.com', 'a8.i.auto.sohu.com', 'sports.sohu.com', 'bmw-m5.i.auto.sohu.com', 'wphone.zone.it.sohu.com', 'mazda5.i.auto.sohu.com', 'sebring.i.auto.sohu.com', 'spirior.i.auto.sohu.com', 'pic.travel.sohu.com', 'ceshi1.i.auto.sohu.com', 'sylphy.i.auto.sohu.com', 'r-class.i.auto.sohu.com', 'apple.zone.it.sohu.com', 'alfaromeo.i.auto.sohu.com', 'mazda3.i.auto.sohu.com', 'zhuanbo.2008.sohu.com', 'vios.i.auto.sohu.com', 'family.i.auto.sohu.com', 'haerbin.auto.sohu.com', 'passat.i.auto.sohu.com', 'xiamen.auto.sohu.com', 'expo2010.sohu.com', 'yeguanyan.i.auto.sohu.com', 'club.city.travel.sohu.com', 'luzun.i.auto.sohu.com', 'daren.women.sohu.com', 'impreza.i.auto.sohu.com', 'yantai206.i.auto.sohu.com', 'cbachina.sports.sohu.com', 'letv.auto.sohu.com', 'p.club.sh.sohu.com', 'bluebird.i.auto.sohu.com', 'infinitiex.i.auto.sohu.com', 'fans.auto.sohu.com', 'coupe2.i.auto.sohu.com', 'kiasoul.i.auto.sohu.com', 'astonmartin.i.auto.sohu.com', 'stock.sohu.com', 'pic.chihe.sohu.com', 'pic.gd.sohu.com', 'spyker.i.auto.sohu.com', 'liana.i.auto.sohu.com', 'pic.v.sohu.com', 'fukang.i.auto.sohu.com', 'csl.sports.sohu.com', 'cr-v.i.auto.sohu.com', 'yule.sohu.com', 'benben.i.auto.sohu.com', 'yubei.i.auto.sohu.com', 'c4.i.auto.sohu.com', 'qq.i.auto.sohu.com', 'jaguar.i.auto.sohu.com', 'avenger.i.auto.sohu.com', 'amg.i.auto.sohu.com', 'astro.sohu.com', 'tiida.i.auto.sohu.com', 'bmwmt.i.auto.sohu.com', 'moinca.i.auto.sohu.com', 'hongtu.i.auto.sohu.com', 'ix35.i.auto.sohu.com', 'galant2.i.auto.sohu.com', 'teamchina.sports.sohu.com', 'chery-a5.i.auto.sohu.com', 'lz.club.sh.sohu.com', 'shenyang.auto.sohu.com', 'pic.cul.sohu.com', 'club.book.sohu.com', 'forte.i.auto.sohu.com', 'sdliaocheng.i.auto.sohu.com', 'sdsx4.i.auto.sohu.com', 'cl-class.i.auto.sohu.com', 'c70.i.auto.sohu.com', 'youngman.i.auto.sohu.com', 'santa-fe.i.auto.sohu.com', 'p.club.astro.sohu.com', 'pic.astro.sohu.com', 'panda.i.auto.sohu.com', 'shenzhen.auto.sohu.com', 'hummer.i.auto.sohu.com', 'camaro.i.auto.sohu.com', 'bmw-x5.i.auto.sohu.com', 'byd.i.auto.sohu.com', 'lz.club.yule.sohu.com', 'r8.i.auto.sohu.com', 'focusfamily.i.auto.sohu.com', 'xiaoguizu.i.auto.sohu.com', 'carnival.i.auto.sohu.com', 'junjiefrv.i.auto.sohu.com', 'yantaicheyou.i.auto.sohu.com', 'men.sohu.com', 'h3.i.auto.sohu.com', 'xinfangban.i.auto.sohu.com', 'outback.i.auto.sohu.com', 'pic.business.sohu.com', 'a6.i.auto.sohu.com', 'feixin.tv.sohu.com', 'polo.i.auto.sohu.com', 't.stock.sohu.com', 'p.club.cul.sohu.com', 'zhangjiakou.auto.sohu.com', 'p.club.news.sohu.com', 'saab9-3.i.auto.sohu.com', 'lotusracer.i.auto.sohu.com', 'octavia.i.auto.sohu.com', 'yanguang.i.auto.sohu.com', 'guanli.i.auto.sohu.com', 's90.i.auto.sohu.com', 'info.2008.sohu.com', 'xian.auto.sohu.com', 'haoqing.i.auto.sohu.com', 'btbdx.i.auto.sohu.com', 'hfcyh.i.auto.sohu.com', 'cherokee.i.auto.sohu.com', 'zzcyh.i.auto.sohu.com', 'bmw-x6.i.auto.sohu.com', 'jaguar-xf.i.auto.sohu.com', 'ford.i.auto.sohu.com', 'bmw-m3.i.auto.sohu.com', 'c5.i.auto.sohu.com', 'sip1288.i.auto.sohu.com', 'cdcyh.i.auto.sohu.com', 'lexusis.i.auto.sohu.com', 'zhuanti.club.travel.sohu.com', 'meirenbao.i.auto.sohu.com', 'riichm1.i.auto.sohu.com', 'touran.i.auto.sohu.com', 'jetta.i.auto.sohu.com', 'qqme.i.auto.sohu.com', 'jingcai.club.sohu.com', 'lz.club.gd.sohu.com', 'club.gd.sohu.com', 'drug.health.sohu.com', 'jsp.auto.sohu.com', 's80.i.auto.sohu.com', 'yaris.i.auto.sohu.com', 'nantong.auto.sohu.com', 'geniss.i.auto.sohu.com', 'campus.learning.sohu.com', 'car022.i.auto.sohu.com', 'saab9-5.i.auto.sohu.com', 'club.mil.news.sohu.com', 'landy.i.auto.sohu.com', 'box.baobao.sohu.com', 'haidian.i.auto.sohu.com', 'club.travel.sohu.com', 'greatwall.i.auto.sohu.com', 'hiace.i.auto.sohu.com', 'cache.club.sohu.com', 'club.learning.sohu.com', 'magotan.i.auto.sohu.com', 'i.auto.sohu.com', 'gongyi.sohu.com', 'c-class.i.auto.sohu.com', 'mil.news.sohu.com', 'perla.i.auto.sohu.com', 'picture.auto.sohu.com', 'index.business.sohu.com', 'huamulan.i.auto.sohu.com', 'lz.news.sohu.com', 'c30.i.auto.sohu.com', 'guba.stock.sohu.com', 'reiz.i.auto.sohu.com', 'qingdao.auto.sohu.com', 'xmcyh.i.auto.sohu.com', 'club.money.sohu.com', 'eos.i.auto.sohu.com', 'tongyue.i.auto.sohu.com', 'huncyh.i.auto.sohu.com', 'cd.club.sohu.com', '300c.i.auto.sohu.com', 'qdcyh.i.auto.sohu.com', 'stock.business.sohu.com', 'chengde.auto.sohu.com', 'zhuanti.club.money.sohu.com', 'it.sohu.com', 'compass.i.auto.sohu.com', 'autofans.i.auto.sohu.com', 'baby.women.sohu.com', 's6.i.auto.sohu.com', 'zhuanti.club.news.sohu.com', 'refine.i.auto.sohu.com', 'roewe350.i.auto.sohu.com', 'geruisi.i.auto.sohu.com', 's-max.i.auto.sohu.com', 'chairman.i.auto.sohu.com', 'saibao3.i.auto.sohu.com', 's-class.i.auto.sohu.com', 'bora.i.auto.sohu.com', 'riichg6.i.auto.sohu.com', 'sip2463.i.auto.sohu.com', 'acyz.i.auto.sohu.com', 'ad2.sh.sohu.com', 'tousu.auto.sohu.com', 'futian.i.auto.sohu.com', 'news.sohu.com', 'changan.i.auto.sohu.com', 'foshan.auto.sohu.com', 'santana.i.auto.sohu.com', 'ask.auto.sohu.com', '207.i.auto.sohu.com', 'music.yule.sohu.com', 'dlcyh.i.auto.sohu.com', 'captiva.i.auto.sohu.com', 'qhdforte.i.auto.sohu.com', 'splash.i.auto.sohu.com', 'nba.sports.sohu.com', 'star.news.sohu.com', 'epica2.i.auto.sohu.com', 'aiyihang.i.auto.sohu.com', 'act1.astro.women.sohu.com', 'jxcyh.i.auto.sohu.com', 'gjjx.i.auto.sohu.com', 'auto.sohu.com', 'rein.i.auto.sohu.com', 'lifan320.i.auto.sohu.com', 'pic.media.sohu.com', 'fengshang.i.auto.sohu.com', 'xingquzu.i.auto.sohu.com', 'club.chihe.sohu.com', 'grand-voyager.i.auto.sohu.com', 'xueche.i.auto.sohu.com', 'teana.i.auto.sohu.com', 'lexusrx.i.auto.sohu.com', 'pic.korea.sohu.com', 'chery.i.auto.sohu.com', 'db.auto.sohu.com', 's60.i.auto.sohu.com', 'zhuanti.club.book.sohu.com', 'jscyh.i.auto.sohu.com', 'zhuanti.club.health.sohu.com', 'digi.it.sohu.com', 'escalade.i.auto.sohu.com', 'zunchi.i.auto.sohu.com', 'bmw-m6.i.auto.sohu.com', 'zhengzhou.auto.sohu.com', 'h2.i.auto.sohu.com', 'mobile.auto.sohu.com']

# print len(url)
# print url.index('roll.sohu.com')

# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# count_v1 = CountVectorizer(stop_words='english', max_df=0.5)
# counts_train = count_v1.fit_transform(newsgroup_train.data)
# print "the shape of train is " + repr(counts_train.shape)

# count_v2 = CountVectorizer(vocabulary=count_v1.vocabulary_)
# counts_test = count_v2.fit_transform(newsgroups_test.data)
# print "the shape of test is " + repr(counts_test.shape)

# tfidftransformer = TfidfTransformer()

# tfidf_train = tfidftransformer.fit(counts_train).transform(counts_train)
# tfidf_test = tfidftransformer.fit(counts_test).transform(counts_test)


# import jieba
# import csv
# fenci = open('./test/fenci/财经.txt'.decode('utf-8'), 'w')  # 数据写入到fenci_key里
zh_stopkey = [line.strip().decode('utf-8')
              for line in open('stop_words.dat').readlines()]

# 读取停止词文件并保存到列表stopkey
# print zh_stopkey
# # key = csv.reader(file('key_ddc.csv', 'rb'))  # 读取需要处理的词库：key_ddc.csv

# key = open('./test/category财经.txt'.decode('utf-8'), 'r').readlines()

# list1 = []
# i = 0

# for keys in key:
#     # print type(keys)
#     keys = keys.strip('[').strip(']').strip()
#     # print keys
#     if i == 0:
#         i = 1
#         # jieba.cut_for_search() 结巴分词搜索引擎模式
#         jiebas = jieba.cut(keys, cut_all=False)
#         # print '/'.join(jiebas)
#         fenci_key = "/".join(list(set(jiebas) - set(stopkey)))  # 使用join链接字符串输出
#         list1.append(fenci_key.strip())  # 将数据添加到list1列表
#         print u'程序处理中，请等待...'
#     else:
#         jiebas = jieba.cut(keys, cut_all=False)
#         fenci_key = "/".join(list(set(jiebas) - set(stopkey)))
#         list1.append(fenci_key.strip())

# zidian = {}.fromkeys(list1).keys()  # 字典去重的方法

# for zd in zidian:
#     try:
#         print zd
#     except:
#         pass
#     fenci.writelines(zd)  # 需要转换成utf-8格式输出
#     fenci.writelines('\n')

# fenci.close()


def stop_words(path='./stop_words.dat'):
    # 中文停用词的列表
    zh_stopkey = [line.strip().decode('utf-8')
                  for line in open(path).readlines()]
    return zh_stopkey


def fenci_test(news):
    """
    输入str类型的新闻，输出分词之后的列表，列表元素是以空格隔开的str类型的新闻

    """
    import jieba
    print type(news)
    if isinstance(news, str):
        res = []
        dealed_news = jieba.cut(news, cut_all=False)
        temp = ' '.join(dealed_news)
        return res.append(temp)
    else:
        res = []
        for e in news:
            dealed_news = jieba.cut(e, cut_all=False)
            temp = ' '.join(dealed_news)
            res.append(temp)
        return res


def deal_test_data(path, filename):
    """
    处理文本，将一个大类数千篇文档集中在一个文本的形式修改为如下形式
    配合scikit-learn中的feature_extraction模块进行分析
    data
    |---cat1
       |---txt1
       |---txt2
       |---...
    |---cat2
           |---txt1
           |---txt2
           |---...
        |---...
    """
    import os

    # 目录是否存在
    if os.path.exists('./%s' % filename):
        pass
    else:
        os.mkdir('./%s' % filename)

    file_list = os.listdir(path)

    for each in file_list:
        count = 0
        file = open(os.path.join(path, each))

        # 把源文件的后缀名去掉
        each = each.strip('.txt')

        if os.path.exists('./%s/%s' % (filename, each)):
            pass
        else:
            os.mkdir('./%s/%s' % (filename, each))

        for line in file.readlines():
            count += 1
            line = line.strip().strip('[').strip(']')
            new_file = open('./%s/%s/%s.txt' %
                            (filename, each, str(count)), 'w')
            dealed_line = jieba.cut(line, cut_all=False)
            new_file.write(' '.join(dealed_line))
            new_file.close()
        file.close()


class news_classify():

    def __init__(self, data_path='./test1', stop_path='./stop_words.dat', test_size=0.1, fs_method='MI', fs_num=20000):

        print 'is dealing with the file'

        # import scipy as sp
        # import numpy as np
        from sklearn.datasets import load_files
        from sklearn.cross_validation import train_test_split
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.feature_extraction.text import CountVectorizer
        import feature_selection

        print 'Loading dataset, %s%% for training, %s%% for testing...' % (str((1 - test_size) * 100), str(test_size * 100))

        self.sohu_news = load_files(data_path)
        self.test_size = test_size

        # 切分数据
        self.doc_terms_train, self.doc_terms_test, self.y_train, self.y_test\
            = train_test_split(self.sohu_news.data, self.sohu_news.target, test_size=self.test_size)

        # print sohu_news.target

        print 'Feature selection...'
        print 'fs method:' + fs_method, 'fs num:' + str(fs_num)
        self.zh_stopkey = stop_words(stop_path)

        self.count_vec = CountVectorizer(
            binary=True, stop_words=self.zh_stopkey)
        self.word_tokenizer = self.count_vec.build_tokenizer()
        self.doc_terms_list_train = [self.word_tokenizer(
            doc_str) for doc_str in self.doc_terms_train]
        self.term_set_fs = feature_selection.feature_selection(
            self.doc_terms_list_train, self.y_train, fs_method)[:fs_num]

        print 'Building VSM model...'
        self.term_dict = dict(
            zip(self.term_set_fs, range(len(self.term_set_fs))))

        # self.vectorizer.fixed_vocabulary = True
        self.count_vec.vocabulary_ = self.term_dict
        self.x_train = self.count_vec.fit_transform(self.doc_terms_train)
        self.x_test = self.count_vec.transform(self.doc_terms_test)

        '''BOOL型特征下的向量空间模型，注意，测试样本调用的是transform接口'''
        # self.count_vec = TfidfVectorizer(binary=False, decode_error='ignore',
        #                                  stop_words=self.zh_stopkey)

        # self.x_train = self.count_vec.fit_transform(self.doc_terms_train)
        # self.x_test = self.count_vec.transform(self.doc_terms_test)
        # pass

        # def text_classifly_twang(dataset_dir_name, fs_method, fs_num):
        #     print 'Loading dataset, 80% for training, 20% for testing...'
        #     movie_reviews = load_files(dataset_dir_name)
        #     doc_str_list_train, doc_str_list_test, doc_class_list_train, doc_class_list_test = train_test_split(
        # movie_reviews.data, movie_reviews.target, test_size=0.2,
        # random_state=0)

        #     print 'Feature selection...'
        #     print 'fs method:' + fs_method, 'fs num:' + str(fs_num)
        #     vectorizer = CountVectorizer(binary=True)
        #     word_tokenizer = vectorizer.build_tokenizer()
        #     doc_terms_list_train = [word_tokenizer(
        #         doc_str) for doc_str in doc_str_list_train]
        #     term_set_fs = feature_selection.feature_selection(
        #         doc_terms_list_train, doc_class_list_train, fs_method)[:fs_num]
        #     print 'Building VSM model...'
        #     term_dict = dict(zip(term_set_fs, range(len(term_set_fs))))
        #     vectorizer.fixed_vocabulary = True
        #     vectorizer.vocabulary_ = term_dict
        #     doc_train_vec = vectorizer.fit_transform(doc_str_list_train)
        #     doc_test_vec = vectorizer.transform(doc_str_list_test)

    def NB(self,):
        # self.vectors_test = count_vec.transform(self.sohu_news.data)
        from sklearn.naive_bayes import MultinomialNB
        from sklearn import metrics
        print '*************************\nNB\n*************************'
        self.NB_clf = MultinomialNB(alpha=.01)
        self.NB_clf.fit(self.x_train, self.y_train)
        # print x_test.toarray()
        self.NB_pred = self.NB_clf.predict(self.x_test)
        print '以%s的数据测试，分类方法NB，效果如下：'.decode('utf-8') % str(self.test_size)
        print 'f1_score', metrics.f1_score(self.y_test, self.NB_pred, average='weighted')
        # print pred

    def KNN(self,):
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn import metrics
        print '*************************\nKNN\n*************************'
        self.knnclf = KNeighborsClassifier()  # default with k=5
        self.knnclf.fit(self.x_train, self.y_train)
        self.KNN_pred = self.knnclf.predict(self.x_test)
        print 'f1_score', metrics.f1_score(self.y_test, self.KNN_pred, average='weighted')
        pass

    def SVM(self):
        from sklearn.svm import SVC
        from sklearn import metrics
        print '*************************\nSVM\n*************************'
        self.svcclf = SVC(kernel='linear')  # default with 'rbf'
        self.svcclf.fit(self.x_train, self.y_train)
        self.svc_pred = self.svcclf.predict(self.x_test)
        # calculate_result(newsgroups_test.target, self.svc_pred)

        print 'f1_score', metrics.f1_score(self.y_test, self.svc_pred, average='weighted')

    def test_news(self, url_path='./url.txt'):

        from sohu_spider import get_url_news

        news = get_url_news(url_path)

        news = fenci_test(news)
        # print news
        x = self.count_vec.transform(news)
        self.test_NB_pred = self.NB_clf.predict(x)
        print '-' * 10 + 'NB test result' + '-' * 10

        # print self.test_NB_pred
        # print type(self.test_NB_pred)
        for i in self.test_NB_pred:
            print 'pred:', self.sohu_news.target_names[i]

    def calculate_result(self, actual, pred):
        m_precision = metrics.precision_score(actual, pred)
        m_recall = metrics.recall_score(actual, pred)
        print 'predict info:'
        print 'precision:{0:.3f}'.format(m_precision)
        print 'recall:{0:0.3f}'.format(m_recall)
        print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, pred))


def feature_select(path):

    import scipy as sp
    import numpy as np
    from sklearn.datasets import load_files
    from sklearn.cross_validation import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer

    '''加载数据集，切分数据集80%训练，20%测试'''

    # sohu_news = load_files('./test1')
    sohu_news = load_files(path)
    test_size = 0.1

    doc_terms_train, doc_terms_test, y_train, y_test\
        = train_test_split(sohu_news.data, sohu_news.target, test_size=test_size)

    print sohu_news.target
    '''BOOL型特征下的向量空间模型，注意，测试样本调用的是transform接口'''
    count_vec = TfidfVectorizer(binary=False, decode_error='ignore',
                                stop_words=zh_stopkey)

    x_train = count_vec.fit_transform(doc_terms_train)

    # ocunt=count_vec.fit_transform(sohu_news.data)
    # print type(x_train)
    # print 'count_vec.shape',ocunt.shape
    # print ocunt.nnz / float(ocunt.shape[0])

    # print x_train

    x_test = count_vec.transform(doc_terms_test)
    print count_vec.vocabulary_
    # print x_test

    # x = count_vec.transform(sohu_news.data)

    # y = sohu_news.target

    # print doc_terms_test.target.shape
    print type(doc_terms_test)
    # print(doc_terms_train[0])

    # print(count_vec.get_feature_names())
    # for i in count_vec.get_feature_names():
    # 	print i
    print len(count_vec.get_feature_names())
    print(x_train.toarray())
    print(sohu_news.target[:5])
    # print y

    # NB做文本分类
    from sklearn.naive_bayes import MultinomialNB
    from sklearn import metrics

    vectors_test = count_vec.transform(sohu_news.data)
    clf = MultinomialNB(alpha=.01)
    clf.fit(x_train, y_train)
    # print x_test.toarray()
    pred = clf.predict(x_test)
    print '以%d的数据做测试，效果如下：' % test_size
    print 'f1_score', metrics.f1_score(y_test, pred, average='weighted')
    print pred

    print '!!!!!!!!!!!!!!!!!!!!!!!'
    from sohu_spider import get_news

    news = get_news('http://stock.sohu.com/20161202/n474784977.shtml')
    print news
    news = fenci_test(news)
    print news
    res = []
    res.append(news)
    x = count_vec.transform(res)
    print x
    pred = clf.predict(x)
    print pred
    print sohu_news.target_names[pred[0]]

    ######################################################
    # KNN Classifier
    from sklearn.neighbors import KNeighborsClassifier
    print '*************************\nKNN\n*************************'
    knnclf = KNeighborsClassifier()  # default with k=5
    knnclf.fit(x_train, y_train)
    pred = knnclf.predict(x_test)
    print 'f1_score', metrics.f1_score(y_test, pred, average='weighted')
    # calculate_result(newsgroups_test.target, pred)

    ######################################################
    # SVM Classifier
    from sklearn.svm import SVC
    print '*************************\nSVM\n*************************'
    svcclf = SVC(kernel='linear')  # default with 'rbf'
    svcclf.fit(x_train, y_train)
    pred = svcclf.predict(x_test)
    # calculate_result(newsgroups_test.target, pred)
    print 'f1_score', metrics.f1_score(y_test, pred, average='weighted')


def calculate_result(actual, pred):
    m_precision = metrics.precision_score(actual, pred)
    m_recall = metrics.recall_score(actual, pred)
    print 'predict info:'
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, pred))


# feature_select('./test1')
# feature_select('./test2')
