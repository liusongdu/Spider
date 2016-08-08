# -*-coding:utf8-*-

from lxml import etree
import os
import re
from namerule import obtainsubfoldername

# Use IE to get the source code
html = '''
<!DOCTYPE html>
<html lang='en' xmlns='http://www.w3.org/1999/xhtml'>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Javascript编程开发视频教程知识体系图_知识体系图</title>
    <meta name="keywords" content="javascript教程,视频教程,web前端开发工程师,javascript下载,javascript经典实例,javascript权威指南,知识体系图,知识体系图" />
    <meta name="description" content="Javascript知识体系图从开发环境搭建开始，介绍Javascript的基础语法、对象、文档对象模型、浏览器对象、高级技巧、AJAX及Javascript设计模式，零基础小白也毫无压力，让你快速入门，掌握Javascript开发技巧。" />
    <link href="http://sp1.jikexueyuan.com/static/css/register.css" rel="stylesheet" type="text/css">
    	<script src="http://hm.baidu.com/hm.js?f3c68d41bda15331608595c98e9c3915"></script>


	<script type="text/javascript" src="http://sp1.jikexueyuan.com/static/scripts/jquery.min.js "></script>










<script type='text/javascript'>
  // 埋点
  var _vds = _vds || [];
  window._vds = _vds;
  (function() {
      _vds.push(['setAccountId', 'aacd01fff9535e79']);

      var jkuid = new RegExp("(^| )uid=([^;]*)(;|$)");
      if (document.cookie.match(jkuid) && document.cookie.match(jkuid)[2]) {
        var uidVal = document.cookie.match(jkuid)[2];
          _vds.push(['setCS1', 'uid', uidVal]);
      }

      (function() {
          var vds = document.createElement('script');
          vds.type = 'text/javascript';
          vds.async = true;
          vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(vds, s);
      })();
  })();
</script>


<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-50413628-1', 'auto');
  ga('send', 'pageview');

</script>
    <link rel="stylesheet" href="http://s1.jikexueyuan.com/common/pkg/common_sync0_libs_4f30de2.css" /><link rel="stylesheet" href="http://s1.jikexueyuan.com/common/pkg/common_sync1_libs_4637308.css" /><link rel="stylesheet" href="http://s1.jikexueyuan.com/common/widget/header/header_d41d8cd.css" /><link rel="stylesheet" href="http://s1.jikexueyuan.com/common/widget/loading/loading_03ba72f.css" /><style type="text/css">.i-lessonState.over,.i-lessonState.underway,.icon,.learnNum:before,.lessonTime:before,.path-matrix>header .over:before,.path-matrix>header .underway:before{background-image:url(http://s1.jikexueyuan.com/path/images/path-elem_9dfc40b.png);background-size:53px 61px}#container>.wrap:after{display:table;clear:both;content:" "}.icon{position:relative;top:-1px;display:inline-block;vertical-align:middle}.i-favorite{width:17px;height:17px;background-position:0 -14px}.i-favorite.ysc,.i-favorite:hover{cursor:pointer;background-position:-17px -14px}.i-favorite.ysc:hover{background-position:-34px -14px}.i-lessonState{position:relative;z-index:10;width:20px;height:20px;display:block;background-color:#35b558;background-image:none;background-repeat:no-repeat}.i-lessonState.null{background-color:#e4e4e4}.i-lessonState.advance{background-color:#11772d}.i-lessonState.advanced{background-color:#053e15}.i-lessonState.over{background-position:0 -31px}.i-lessonState.underway{background-position:-20px -31px}.path-describe{margin:0 0 28px;padding:14px;border:1px solid #e4e4e4}.path-describe>header{padding:0 0 12px;border-bottom:1px solid #e4e4e4}.path-describe>header:after{display:table;clear:both;content:" "}.path-describe>header h2{float:left;color:#666;font-size:20px;line-height:34px}.path-describe>header h2 img{position:relative;top:-2px;height:25px;margin:0 10px 0 0}.path-describe>header .mod-tips{float:left;margin:10px 0 0 20px}.path-describe>header h3{color:#35b558;font-size:18px;line-height:20px}.path-describe>.bd:after{display:table;clear:both;content:" "}.practice-text{margin:0;background:#f8f8f8}.practice-text .bd p{float:left;width:780px;padding:12px 0 0;color:#666;font-size:12px;line-height:24px}.practice-text .bd .btn{float:right;display:inline-block;width:144px;height:40px;margin:29px 7px 0 0;background:#35b558;color:#fff;font-size:18px;line-height:40px;text-align:center;-webkit-transition:background-color .8s;-moz-transition:background-color .8s;transition:background-color .8s}.practice-text .bd .btn:hover{background:#66d178}.path-matrix>header{padding:16px 0;line-height:40px}.path-matrix>header:after{display:table;clear:both;content:" "}.path-matrix>header h3{float:left;color:#35b558}.path-matrix>header aside{float:right;color:#666;text-align:right;font-size:12px}.path-matrix>header aside span{margin-left:20px}.path-matrix>header aside span:before{position:relative;top:-1px;display:inline-block;width:10px;height:10px;-webkit-border-radius:50%;-moz-border-radius:50%;border-radius:50%;margin-right:5px;background:#35b558;content:" ";vertical-align:middle}.path-matrix>header .advance:before{background:#11772d}.path-matrix>header .advanced:before{background:#053e15}.path-matrix>header .null:before{background:#e4e4e4}.path-matrix>header .over:before,.path-matrix>header .underway:before{background-color:transparent;background-repeat:no-repeat;background-position:0 -51px}.path-matrix>header .underway:before{background-position:-10px -51px}#pathMatrix>header section{display:none;clear:both}#pathMatrix>header section p{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;width:100%;max-height:66px;color:#666;font-size:12px;line-height:22px}#pathMatrix>header .mod-tips{display:inline-block;vertical-align:middle;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}#pathMatrix>header .mod-tips .icon{margin-right:6px;cursor:pointer}#pathMatrix>header .tips-help .icon{width:14px;height:14px;background:#999;background-image:none;-webkit-border-radius:50%;-moz-border-radius:50%;border-radius:50%;color:#fff;font:12px/14px arial}.mod-matrix ul{margin:0 -5px -5px 0}.mod-matrix ul:after{display:table;clear:both;content:" "}.mod-matrix li{overflow:visible;float:left;width:20px;height:20px;margin:0 5px 5px 0}.mod-matrix .i-lessonState{overflow:hidden}.mod-matrix .i-lessonState .mod-lesson{opacity:0;position:absolute;bottom:100%;left:-145px;width:310px}.mod-matrix .i-lessonState .mod-lesson .joint{display:block;content:" ";height:14px;width:32px;position:absolute;top:100%;left:50%;margin:0 0 0 -16px}.mod-matrix .i-lessonState .mod-lesson h3{text-indent:0;padding:0}.mod-matrix li.hover .i-lessonState{overflow:visible;z-index:1200}.mod-matrix li.hover .i-lessonState .mod-lesson{visibility:visible;opacity:1}.mod-matrix .i-lessonState .mod-lesson,.mod-matrix .i-lessonState .mod-lesson:hover{visibility:visible;overflow:visible;height:175px;padding:12px 14px;margin:0 0 9px;border:1px solid #e4e4e4;background:#fff}.mod-matrix .i-lessonState .mod-lesson .other,.mod-matrix .i-lessonState .mod-lesson p,.mod-matrix .i-lessonState .mod-lesson:hover .other,.mod-matrix .i-lessonState .mod-lesson:hover p{opacity:1;visibility:visible}.mod-matrix .i-lessonState .mod-lesson h3,.mod-matrix .i-lessonState .mod-lesson:hover h3{height:40px;white-space:normal}#path{margin:0 0 22px}.path-item{margin:0 0 28px;position:relative}.path-item h2{margin:0 0 5px;color:#666;font-size:18px;line-height:22px}.path-item>header{padding:0 0 15px}.path-item>header .describe{color:#999;font-size:12px;line-height:16px}.path-item>header .lessonTime{float:right;color:#666}.path-item>header .lessonTime em{color:#f90;margin-right:6px}.lessons{border:1px solid #e4e4e4;padding:14px 14px 0}.lessons:after{display:table;clear:both;content:" "}.lessons .l-item{float:left;width:316px;height:20px;margin:0 11px 20px 0}.mod-lesson{position:relative;z-index:20;overflow:hidden;height:20px;-webkit-transition:height .3s;-moz-transition:height .3s;-ms-transition:height .3s;transition:height .3s}.mod-lesson>dl:after{display:table;clear:both;content:" "}.mod-lesson>dl>dt{float:left;width:20px}.mod-lesson>dl>dd{margin-left:28px}.mod-lesson h3{overflow:hidden;text-overflow:ellipsis;height:20px;margin:0 0 12px;padding:0 0 0 1.1em;color:#333;font-size:14px;line-height:20px;text-indent:-1.1em;white-space:nowrap;cursor:default}.mod-lesson h3 a{color:#333}.mod-lesson h3 a:hover{color:#35b558}.mod-lesson .other,.mod-lesson p{-webkit-transition:opacity .3s .1s;-moz-transition:opacity .3s .1s;-ms-transition:opacity .3s .1s;transition:opacity .3s .1s}.mod-lesson p{visibility:hidden;opacity:0;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;width:100%;height:60px;margin:0 0 20px;color:#666;font-size:12px;line-height:20px;word-break:break-all}.mod-lesson .other{visibility:hidden;opacity:0;padding:0 0 4px;color:#999;font-size:12px;line-height:14px}.mod-lesson .other>span{display:inline-block;margin:0 14px 0 0;white-space:nowrap}.mod-lesson .other>.learnNum,.mod-lesson .other>.lessonTime{width:120px}.mod-lesson .other>.learnNum{margin-right:0}.mod-lesson .other .i-favorite{float:right;margin:0 4px 0 0}.mod-lesson .learnNum:before,.mod-lesson .lessonTime:before{position:relative;top:-1px;display:inline-block;width:14px;height:14px;margin-right:5px;background-position:0 0;content:" ";vertical-align:middle}.mod-lesson .learnNum:before{background-position:-14px 0}.mod-lesson>.arrow{position:absolute;top:100%;left:50%;margin:0 0 0 -8px}.mod-lesson>.arrow:after,.mod-lesson>.arrow:before{display:block;width:0!important;height:0!important;padding:0!important;font-size:0!important;line-height:0!important;border:8px solid transparent;border-bottom-width:0;border-top-color:#e4e4e4;content:" "}.mod-lesson>.arrow:after{position:absolute;bottom:1px;left:1px;border-width:7px;border-bottom-width:0;border-top-color:#fff}.mod-lesson:hover{z-index:100;overflow:visible;height:175px;margin:-11px -8px -11px -11px;padding:10px 7px 10px 10px;background:#f8f8f8;border:1px solid #e4e4e4}.mod-lesson:hover h3{height:40px;white-space:normal}.mod-lesson:hover .other,.mod-lesson:hover p{opacity:1;visibility:visible}.lessons .l-item:nth-child(3n+3){margin-right:0}.pathdescibe{border:1px solid #e4e4e4;padding:15px}.pathdescibe>img{display:block;width:50px;float:left}.pathdescibe h1{font-size:22px;color:#333;margin-left:65px;margin-bottom:10px;font-weight:500}.pathdescibe p{font-size:12px;color:#666;line-height:20px;margin-left:65px}.pathstage .pathstage-txt{text-align:center;line-height:22px}.pathstage .pathstage-txt h2{font-size:14px;color:#333;font-weight:500}.pathstage .pathstage-txt p{font-size:12px;color:#666}.pathstage .pathstage-txt span{font-size:12px;color:#666}.pathstage .stagebox{border:1px solid #e4e4e4;width:100%}.pathstage .stagebox .stagewidth{width:1100px}.pathstage .lesson-list ul{width:auto!important;margin-top:0!important;margin-left:-1px;margin-bottom:-1px}.pathstage .lesson-list ul li{margin-right:0!important;margin-bottom:0!important;width:250px!important;height:240px!important;padding:10px;border-bottom:1px solid #E4E4E4;border-right:1px solid #E4E4E4}.pathstage .lesson-list .lessonimg-box{width:230px!important;border:1px solid #fff}.pathstage .lesson-list .lesson-infor{border:0!important}.page-oneicon{width:100%;height:30px;text-align:center;position:relative}.page-oneicon img{position:absolute;top:0;left:50%;margin-left:-7px}.page-oneicon i{display:block;background:#dcdcdc;border-radius:50%;width:10px;height:10px;margin:0 auto}.page-oneicon div{border-right:1px solid #dcdcdc;width:50%;height:20px}.pathstage .stage-more{height:40px;cursor:pointer;font-size:12px;background:#f7f7f7;color:#333;text-align:center;line-height:40px}.over{font-size:12px;color:#333;text-align:center;padding-top:10px;font-weight:400}</style></head>
    <body>
        <div id="wrapper">
        <script src="http://e.jikexueyuan.com/static/js/browser.js"></script>
<script src="http://e.jikexueyuan.com/static/js/growingio.js"></script>
<script src="http://sp1.jikexueyuan.com/static/scripts/jquery.min.js"></script>
<link rel="stylesheet" href="http://e.jikexueyuan.com/headerandfooter/css/header.css" />
<div id="header">
	<div class="w-1000 relative">
		<a href="http://www.jikexueyuan.com" class="logo"><img src="http://e.jikexueyuan.com/headerandfooter/images/logo.png" height="40" width="109" /></a>
		<!--nav-->
		<nav>
			<ul>
				<li><a href="http://www.jikexueyuan.com">首页</a></li>
				<li>职业学院<i class="arrow-icon"></i>
					<div class="submenu school-list">
						<h3>前端学院</h3>
						<a href="http://www.jikexueyuan.com/zhiye/web"><i class="web-icon"></i>Web 前端工程师</a>
						<!--<a href="#"><i class="android-icon"></i>web大前端</a>-->
						<h3>后端学院</h3>
						<a href="http://www.jikexueyuan.com/zhiye/python"><i class="python-icon"></i>Python Web工程师</a>
						<a href="http://www.jikexueyuan.com/zhiye/go"><i class="go-icon"></i>Go语言工程师</a>
						<!--<a href="http://j.jikexueyuan.com/train/php?huodong=jiuye_php_in"><i class="php-icon"></i>PHP工程师</a>
						<a href="http://j.jikexueyuan.com/train/javaweb?huodong=jiuye_javaweb_guide"><i class="java-icon"></i>Java Web工程师</a>-->
						<h3>移动学院</h3>
						<a href="http://www.jikexueyuan.com/zhiye/ios"><i class="ios-icon"></i>iOS工程师</a>
						<!--<a href="http://j.jikexueyuan.com/train/android?huodong=jiuye_android_in"><i class="android-icon"></i>Android 开发工程师</a>-->

					</div>
				</li>
				<li>会员课程<i class="arrow-icon"></i>
					<div class="submenu vip-lesson">
						<a href="http://www.jikexueyuan.com/course/"><i class="kck-icon"></i>课程库<span>2500+</span></a>
						<a href="http://ke.jikexueyuan.com/zhiye/"><i class="zyljt-icon"></i>职业路径图<span>9</span></a>
						<a href="http://www.jikexueyuan.com/path/"><i class="zstxt-icon"></i>知识体系图<span>24</span></a>
						<a href="http://ke.jikexueyuan.com/xilie/"><i class="xlkc-icon"></i>系列课程<span>101</span></a>
						<a href="http://www.jikexueyuan.com/tag/"><i class="kcbq-icon"></i>课程标签<span>4000+</span></a>
						<a href="http://www.jikexueyuan.com/vip/"><i class="vip-icon"></i>VIP会员购买<span>30/月  260/年</span></a>

					</div>
				</li>
				<li>极客社区<i class="arrow-icon"></i>
					<div class="submenu vip-lesson">
						<a href="http://wenda.jikexueyuan.com"><i class="jswd-icon"></i>技术问答<span>20000+</span></a>
						<a href="http://wiki.jikexueyuan.com"><i class="wiki-icon"></i>Wiki<span>351</span></a>
						<a href="http://qun.jikexueyuan.com"><i class="sq-icon"></i>社群<span>7000+</span></a>
						<a href="http://download.jikexueyuan.com"><i class="zygx-icon"></i>资源下载<span>3000+</span></a>
					</div>
				</li>
			</ul>
		</nav>
		<!--nav end-->
		<!--login-->
		<div class="icon-box">
			<span class="search-icon" id="search-btn"></span>
			<span class="app-icon loginlist relative" id="appicon">
					<div class="submenu">
						<i class="top-icon"></i>
						<img src="http://e.jikexueyuan.com/headerandfooter/images/heade-rwm.png" />
					</div>
				</span>
			<span class="relative loginlist" id="loginlist">
						<!--<dl class="submenu">
							<i class="top-icon"></i>
							<dd><a href="http://passport.jikexueyuan.com/sso/reg_phone" class="reg-btn">注册</a>|<a href="http://passport.jikexueyuan.com/sso/login" class="login-btn">登录</a></dd>
							<dd><a href="#"><i class="xxzx-icon"></i>学习中心</a></dd>
							<dd><a href="http://my.jikexueyuan.com/"><i class="grzy-icon"></i>个人主页</a></dd>
							<dd><a href="http://www.jikexueyuan.com/member/notifications/"><i class="xxtz-icon"></i>消息通知</a></dd>
							<dd><a href="http://my.jikexueyuan.com/setting/user/"><i class="zhsz-icon"></i>账号设置</a></dd>
						</dl>-->
					</span>

		</div>
		<!--login-->
		<!--searchbox-->
		<div class="searchbox" id="searchbox">
			<i class="close-icon" id="close-btn"></i>
			<i class="search-icon" id="search-btn"></i>
			<input id="web_search_header" placeholder="搜索课程、问答或Wiki" value="">
			<div class="tagbox">
				<a href="http://search.jikexueyuan.com/course/?q=Android">Android</a>
				<a href="http://search.jikexueyuan.com/course/?q=iOS">iOS</a>
				<a href="http://search.jikexueyuan.com/course/?q=HTML5">HTML5</a>
			</div>
		</div>
	</div>
</div>
<script src="http://e.jikexueyuan.com/headerandfooter/js/header.min.js"></script>
<script src="http://e.jikexueyuan.com/headerandfooter/js/web_socket.js"></script>
<script src="http://e.jikexueyuan.com/headerandfooter/js/websocket.js?v=6.0"></script>

            <div  id="pager">

	<div id="container">
	<div class="wrap w-1000">
		<!-- crumbs-->
		<div class="crumbs">
			<div class="w-1000">
				<a href="http://www.jikexueyuan.com">首页</a>
				<em>&gt;</em>
				<a href="http://www.jikexueyuan.com/path/" jktag="&posGP=1001003&posArea=0004&posOper=24007&posColumns=4.1">知识体系图</a>
				<em>&gt;</em>JavaScript
			</div>
		</div>
		<!-- crumbs-->
		  <div class = "lesson_loading">
        <div class="spinner">
          <div class="rect1"></div>
          <div class="rect2"></div>
          <div class="rect3"></div>
          <div class="rect4"></div>
          <div class="rect5"></div>
        </div>
        <div class="txt">课程加载中...</div>
  </div>

		<!--pathdescibe-->
		<div class="pathdescibe" style="display: none;">
			<img src="http://a1.jikexueyuan.com/home/201603/14/2f8a/56e619ce2f043.png" />
			<h1>JavaScript开发知识体系图</h1>
			<p>


			</p>
		</div>
		<!--pathdescibe-->

		<!--pathstage -->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>1. JavaScript 开发前的准备</h2>
				<p>本阶段主要是 JavaScript 的简介、开发环境搭建、常用调试工具和调试方法。</p>
				<span>(共1课程，47分钟，17706人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =0.25>



<li id="65" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/65.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=65&posColumn=65.1">
			<img src="http://a1.jikexueyuan.com/home/201405/20/135d/537a80597f629.jpg" class="lessonimg" title="Javascript基础语法、数组、面向对象、调试" alt="Javascript基础语法、数组、面向对象、调试">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=65&posColumn=65.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/65.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=65&posColumn=65.1">Javascript基础语法、数组、面向对象、调试</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课学习掌握Javascript的基本技术，改进网页的应用。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>8课时
							47分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">17706人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=65&posColumn=65.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_0">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>2. JavaScript 基础语法</h2>
				<p>本阶段主要介绍 JavaScript 语言的初级知识和基本的语法概念等。</p>
				<span>(共3课程，94分钟，123559人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =0.75>



<li id="179" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/179.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=179&posColumn=179.1">
			<img src="http://a1.jikexueyuan.com/home/201408/07/cc68/53e37a8089faa.jpg" class="lessonimg" title="JavaScript基础教程" alt="JavaScript基础教程">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=179&posColumn=179.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/179.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=179&posColumn=179.1">JavaScript基础教程</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课讲解JavaScript基础知识，让学员了解到什么是JavaScript，并且了解它的语法和变量。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							24分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">53468人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=179&posColumn=179.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="178" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/178.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=178&posColumn=178.2">
			<img src="http://a1.jikexueyuan.com/home/201408/07/6b61/53e37a9abd818.jpg" class="lessonimg" title="JavaScript语法详解" alt="JavaScript语法详解">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=178&posColumn=178.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/178.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=178&posColumn=178.2">JavaScript语法详解</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课讲解JavaScript语法，让学员掌握运算符、控制语句和循环语句可以让你对js有一个全面的认识。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>7课时
							41分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">36242人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=178&posColumn=178.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="180" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/180.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=180&posColumn=180.3">
			<img src="http://a1.jikexueyuan.com/home/201408/10/bd8c/53e7059c107e4.jpg" class="lessonimg" title="JavaScript函数" alt="JavaScript函数">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=180&posColumn=180.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/180.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=180&posColumn=180.3">JavaScript函数</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScript函数，让学员掌握函数的应用以及变量的作用域
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>6课时
							29分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">33849人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=180&posColumn=180.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_1">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>3. JavaScript 对象</h2>
				<p>JavaScript是一种基于对象的脚本语言,它不仅可以创建对象,也能使用现有的对象。本阶段主要讲解 JavaScript 对象的核心思想及常用内置对象的使用。</p>
				<span>(共3课程，94分钟，62144人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =0.75>



<li id="210" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/210.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=210&posColumn=210.1">
			<img src="http://a1.jikexueyuan.com/home/201408/25/7eeb/53fae6449c8ce.jpg" class="lessonimg" title="JavaScript面向对象详解" alt="JavaScript面向对象详解">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=210&posColumn=210.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/210.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=210&posColumn=210.1">JavaScript面向对象详解</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScript的面向对象，让学员能更好的设计代码。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							25分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">24786人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=210&posColumn=210.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="195" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/195.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=195&posColumn=195.2">
			<img src="http://a1.jikexueyuan.com/home/201408/17/c479/53f059c7d1e10.jpg" class="lessonimg" title="JavaScript内置对象" alt="JavaScript内置对象">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=195&posColumn=195.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/195.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=195&posColumn=195.2">JavaScript内置对象</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScript的内置对象，包括字符串、日期对象、数组对象和Math对象。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>5课时
							38分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">24228人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=195&posColumn=195.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1379" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1379.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1379&posColumn=1379.3">
			<img src="http://a1.jikexueyuan.com/home/201604/25/1966/571dd2f73ea5c.jpg" class="lessonimg" title="JavaScript正则表达式" alt="JavaScript正则表达式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1379&posColumn=1379.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1379.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1379&posColumn=1379.3">JavaScript正则表达式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程学习JavaScript正则表达式，正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp或RE）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串搜索模式。搜索模式可用于文本搜索和文本替换。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							31分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon2"></i><em>中级</em>
					</dd>

				</dl>
				<em class="learn-number">13130人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1379&posColumn=1379.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_2">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>4. JavaScript 文档对象模型</h2>
				<p>本阶段主要介绍如何使用 JavaScript 控制 DOM 树。</p>
				<span>(共3课程，72分钟，76357人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =0.75>



<li id="185" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/185.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=185&posColumn=185.1">
			<img src="http://a1.jikexueyuan.com/home/201408/12/cdb8/53ea16bcd7f0f.jpg" class="lessonimg" title="JavaScript DOM对象" alt="JavaScript DOM对象">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=185&posColumn=185.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/185.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=185&posColumn=185.1">JavaScript DOM对象</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScriptDOM对象，通过对DOM对象的使用操作HTML和CSS
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							24分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">29597人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=185&posColumn=185.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="207" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/207.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=207&posColumn=207.2">
			<img src="http://a1.jikexueyuan.com/home/201408/24/95ec/53f9ea6933be5.jpg" class="lessonimg" title="JavaScript DOM对象控制HTML元素详解" alt="JavaScript DOM对象控制HTML元素详解">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=207&posColumn=207.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/207.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=207&posColumn=207.2">JavaScript DOM对象控制HTML元素详解</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScript的DOM对象控制HTML元素，从而能更好的对页面进行操作。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>2课时
							22分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">21070人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=207&posColumn=207.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="196" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/196.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=196&posColumn=196.3">
			<img src="http://a1.jikexueyuan.com/home/201408/17/9dc9/53f05ce862437.jpg" class="lessonimg" title="JavaScript事件详解" alt="JavaScript事件详解">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=196&posColumn=196.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/196.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=196&posColumn=196.3">JavaScript事件详解</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课讲解JavaScript对事件的处理，了解几种事件的应用以及在不同浏览器中的兼容性。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							26分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">25690人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=196&posColumn=196.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_3">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>5. JavaScript 浏览器对象</h2>
				<p>本阶段主要介绍 JavaScript 是如何与浏览器进行“对话”的，能为开发提供很多便捷。</p>
				<span>(共1课程，30分钟，20414人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =0.25>



<li id="208" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/208.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=208&posColumn=208.1">
			<img src="http://a1.jikexueyuan.com/home/201408/24/6a01/53f9ece25b4c0.jpg" class="lessonimg" title="JavaScript浏览器对象" alt="JavaScript浏览器对象">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=208&posColumn=208.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/208.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=208&posColumn=208.1">JavaScript浏览器对象</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课主要讲解JavaScript的浏览器对象，包括计时器、History、Location和Cookies等
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>5课时
							30分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">20414人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=208&posColumn=208.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_4">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>6. JavaScript 高级技巧</h2>
				<p>本阶段主要介绍 JS 开发中常用的库和一些技巧，帮助开发者提高技术水平。</p>
				<span>(共8课程，266分钟，104979人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =2>



<li id="184" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/184.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=184&posColumn=184.1">
			<img src="http://a1.jikexueyuan.com/home/201408/12/abbe/53ea0675f1114.jpg" class="lessonimg" title="JavaScript异常处理和事件处理" alt="JavaScript异常处理和事件处理">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=184&posColumn=184.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/184.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=184&posColumn=184.1">JavaScript异常处理和事件处理</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课讲解JavaScript异常和事件，让学员学习到出现异常如何处理以及事件的触发
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>2课时
							21分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">28763人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=184&posColumn=184.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="218" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/218.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=218&posColumn=218.2">
			<img src="http://a1.jikexueyuan.com/home/201408/31/1bf7/540335cc92248.jpg" class="lessonimg" title="Javascript瀑布流" alt="Javascript瀑布流">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=218&posColumn=218.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/218.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=218&posColumn=218.2">Javascript瀑布流</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			通过JS实现瀑布流效果
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							47分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">24150人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=218&posColumn=218.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/practice/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/advance.png" alt="practice" title="项目实战" jktag="&posGP=101001&posArea=&posOper=&aCId=218&posColumn=218.2&aCCate=practice" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="840" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/840.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=840&posColumn=840.3">
			<img src="http://a1.jikexueyuan.com/home/201505/06/2179/55496d4bd417a.jpg" class="lessonimg" title="JavaScript 模块化" alt="JavaScript 模块化">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=840&posColumn=840.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/840.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=840&posColumn=840.3">JavaScript 模块化</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍常用的模块化开发的库包括 seajs 和 requirejs 以及模块化的概念。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							32分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon2"></i><em>中级</em>
					</dd>

				</dl>
				<em class="learn-number">9911人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=840&posColumn=840.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1249" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1249.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1249&posColumn=1249.4">
			<img src="http://a1.jikexueyuan.com/home/201506/03/c565/556e586bcd37b.jpg" class="lessonimg" title="JavaScript面向切面编程" alt="JavaScript面向切面编程">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1249&posColumn=1249.4"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1249.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1249&posColumn=1249.4">JavaScript面向切面编程</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍JavaScript面向切面编程，让同学门可以进行无侵入式的编程。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							26分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">6426人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1249&posColumn=1249.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1272" test="0" deg="0" >
	<div class="lessonimg-box">



		<a href="http://www.jikexueyuan.com/course/1272.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1272&posColumn=1272.5">
			<img src="http://a1.jikexueyuan.com/home/201506/04/87d3/55703eac8d4f5.jpg" class="lessonimg" title="JavaScript高级函数" alt="JavaScript高级函数">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1272&posColumn=1272.5"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1272.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1272&posColumn=1272.5">JavaScript高级函数</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍JavaScript常用的高级函数，主要包括惰性载入函数、函数柯里化、级联函数。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							26分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">11396人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1272&posColumn=1272.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1313" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1313.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1313&posColumn=1313.6">
			<img src="http://a1.jikexueyuan.com/home/201506/10/47ca/5577921a05d66.jpg" class="lessonimg" title="JavaScript高级技巧" alt="JavaScript高级技巧">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1313&posColumn=1313.6"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1313.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1313&posColumn=1313.6">JavaScript高级技巧</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程学习JavaScript高级技巧
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							27分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">8709人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1313&posColumn=1313.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1329" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1329.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1329&posColumn=1329.7">
			<img src="http://a1.jikexueyuan.com/home/201506/11/bceb/5578e0e01a405.jpg" class="lessonimg" title="JavaScript数据推送" alt="JavaScript数据推送">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1329&posColumn=1329.7"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1329.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1329&posColumn=1329.7">JavaScript数据推送</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍JavaScript数据推送
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							49分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon2"></i><em>中级</em>
					</dd>

				</dl>
				<em class="learn-number">8444人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1329&posColumn=1329.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1442" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1442.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1442&posColumn=1442.8">
			<img src="http://a1.jikexueyuan.com/home/201506/24/a082/558a11c35f925.jpg" class="lessonimg" title="JavaScript多线程" alt="JavaScript多线程">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1442&posColumn=1442.8"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1442.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1442&posColumn=1442.8">JavaScript多线程</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程学习JavaScript多线程，在HTML5 webwork没出现之前很多人都是用ConcurrentThread.js模拟多线程。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							38分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon2"></i><em>中级</em>
					</dd>

				</dl>
				<em class="learn-number">7180人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1442&posColumn=1442.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_5">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>7. AJAX</h2>
				<p>本阶段课程主要讲解了AJAX的概念以及相关API，讲解了通用代码封装、使用AJAX时的常见问题与解决方案，及跨域AJAX的相关内容。通过本系统课程学习，学员可以全面掌握AJAX相关知识并应用于实践。</p>
				<span>(共6课程，355分钟，47327人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =1.5>



<li id="1919" test="0" deg="0" >
	<div class="lessonimg-box">



		<a href="http://www.jikexueyuan.com/course/1919.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1919&posColumn=1919.1">
			<img src="http://a1.jikexueyuan.com/home/201508/31/3607/55e3b20110acb.jpg" class="lessonimg" title="基于 Node.js 的后端应用简介" alt="基于 Node.js 的后端应用简介">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1919&posColumn=1919.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1919.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1919&posColumn=1919.1">基于 Node.js 的后端应用简介</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			AJAX 请求需要后端程序的配合，不了解完整的请求处理过程会很难透彻地理解 AJAX。本课程首先简要介绍 HTTP 的相关知识，然后介绍一个简单的 Node.js 应用，以便没有后端开发基础的学员也能快速使用这个应用来实践后续的 AJAX 课程。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							44分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">6389人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/express/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/nodedotjs.png" alt="express" title="express" jktag="&posGP=101001&posArea=&posOper=&aCId=1919&posColumn=1919.1&aCCate=express" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="2038" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/2038.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2038&posColumn=2038.2">
			<img src="http://a1.jikexueyuan.com/home/201509/18/05c8/55fb6bf5a35bb.jpg" class="lessonimg" title="AJAX 基础" alt="AJAX 基础">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=2038&posColumn=2038.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/2038.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2038&posColumn=2038.2">AJAX 基础</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程主要讲解 AJAX 基础知识，首先介绍 AJAX 的概念、应用场景及相关技术，然后对相关的 API 做详细讲解。学习本课后，学员可完全掌握 AJAX 的原理与使用方法。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>5课时
							49分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">12449人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=2038&posColumn=2038.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="2087" test="0" deg="0" >
	<div class="lessonimg-box">



		<a href="http://www.jikexueyuan.com/course/2087.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2087&posColumn=2087.3">
			<img src="http://a1.jikexueyuan.com/home/201509/28/4265/56089bd38fe3c.jpg" class="lessonimg" title="AJAX-通用代码封装与常见问题处理" alt="AJAX-通用代码封装与常见问题处理">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=2087&posColumn=2087.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/2087.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2087&posColumn=2087.3">AJAX-通用代码封装与常见问题处理</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			使用 AJAX 时，程序代码模式固定，将公共固定部分的代码封装起来，在后续使用时直接调用，可避免每次都机械重复的编写代码。另外，在使用 AJAX 方式编程时，会遇到一些区别于传统方式的问题。本课程首先讲解代码封装，然后介绍使用 AJAX 时的常见问题与解决方案。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>5课时
							84分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">5331人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=2087&posColumn=2087.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="2185" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/2185.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2185&posColumn=2185.4">
			<img src="http://a1.jikexueyuan.com/home/201510/28/347d/5630294ac281b.jpg" class="lessonimg" title="在 jQuery 中使用 AJAX" alt="在 jQuery 中使用 AJAX">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=2185&posColumn=2185.4"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/2185.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2185&posColumn=2185.4">在 jQuery 中使用 AJAX</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			jQuery 是当前应用最广泛的 JavaScript 库，它提供了大量 AJAX API，提升了 AJAX 使用的便利性，本课程详细讲解 jQuery AJAX 相关 API 的使用。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							92分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">9658人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/jquery/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/c538/575cd38804558.png" alt="jquery" title="jQuery" jktag="&posGP=101001&posArea=&posOper=&aCId=2185&posColumn=2185.1&aCCate=jquery" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="2209" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/2209.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2209&posColumn=2209.5">
			<img src="http://a1.jikexueyuan.com/home/201511/03/f248/56380eb822bd3.jpg" class="lessonimg" title="跨域 AJAX 的实现" alt="跨域 AJAX 的实现">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=2209&posColumn=2209.5"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/2209.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2209&posColumn=2209.5">跨域 AJAX 的实现</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			基于 JavaScript 的同源策略，默认情况下不允许向其它域发起 AJAX 请求，但在开发过程，经常会有跨域的需求。本课程详细讲解各种常见跨域 AJAX 的实现方案。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							52分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">5913人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=2209&posColumn=2209.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="2224" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/2224.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2224&posColumn=2224.6">
			<img src="http://a1.jikexueyuan.com/home/201511/05/a6ca/563ab7673d420.jpg" class="lessonimg" title="AJAX 文件上传" alt="AJAX 文件上传">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=2224&posColumn=2224.6"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/2224.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=2224&posColumn=2224.6">AJAX 文件上传</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程讲解两种无刷新页面文件上传实现方式，一种是利用 XMLHttpRequest Level 2 新增的 upload 对象，另一种是利用 iframe 伪 AJAX 方式。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>3课时
							34分钟</em>
					</dd>
					<dd class="zhongji">

						<i class="xinhao-icon"></i><em>初级</em>
					</dd>

				</dl>
				<em class="learn-number">7587人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=2224&posColumn=2224.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_6">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

		<div class="pathstage mar-t30" style="display: none;">
			<div class="pathstage-txt">
				<h2>8. JavaScript 设计模式</h2>
				<p>本阶段主要介绍了各种设计模式在 JavaScript 中的应用，是软件设计与架构的基本，指导开发者编写简洁、可复用、高可靠的代码。</p>
				<span>(共18课程，348分钟，101722人已经学习)</span>
			</div>
			<div class="page-oneicon mar-t10">
				<i></i>
				<div></div>
			</div>

			<div class="stagebox ">
				<div class="stagewidth lesson-list" style="display: block;">
					<ul class="cf" showNumber =4.5>



<li id="652" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/652.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=652&posColumn=652.1">
			<img src="http://a1.jikexueyuan.com/home/201503/31/44b1/551a09c62449c.jpg" class="lessonimg" title="JavaScript 设计模式简介" alt="JavaScript 设计模式简介">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=652&posColumn=652.1"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/652.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=652&posColumn=652.1">JavaScript 设计模式简介</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本节课主要学习设计模式基础概念和设计原则。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							18分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">12325人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=652&posColumn=652.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=652&posColumn=652.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="655" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/655.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=655&posColumn=655.2">
			<img src="http://a1.jikexueyuan.com/home/201504/01/1bfd/551b4e48c0e2a.jpg" class="lessonimg" title="JavaScript 设计模式之工厂模式" alt="JavaScript 设计模式之工厂模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=655&posColumn=655.2"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/655.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=655&posColumn=655.2">JavaScript 设计模式之工厂模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程学习工厂模式,工厂模式定义一个用于创建对象的接口，这个接口由子类决定实例化哪一个类。该模式使一个类的实例化延迟到了子类。而子类可以重写接口方法以便创建的时候指定自己的对象类型(抽象工厂)。

		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>5课时
							23分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">7735人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=655&posColumn=655.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=655&posColumn=655.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="673" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/673.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=673&posColumn=673.3">
			<img src="http://a1.jikexueyuan.com/home/201504/07/feeb/55233a4c24261.jpg" class="lessonimg" title="JavaScript 设计模式之单例模式" alt="JavaScript 设计模式之单例模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=673&posColumn=673.3"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/673.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=673&posColumn=673.3">JavaScript 设计模式之单例模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍单例模式，单例就是保证一个类只有一个实例，实现的方法一般是先判断实例存在与否，如果存在直接返回，如果不存在就创建了再返回，这就确保了一个类只有一个实例对象。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							25分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">8702人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=673&posColumn=673.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=673&posColumn=673.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="720" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/720.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=720&posColumn=720.4">
			<img src="http://a1.jikexueyuan.com/home/201504/14/7239/552c72089e2d6.jpg" class="lessonimg" title="Javascript 设计模式之构造函数模式" alt="Javascript 设计模式之构造函数模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=720&posColumn=720.4"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/720.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=720&posColumn=720.4">Javascript 设计模式之构造函数模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程学习构造函数模式,构造函数用于创建特定类型的对象——不仅声明了使用的对象，构造函数还可以接受参数以便第一次创建对象的时候设置对象的成员值。你可以自定义自己的构造函数，然后在里面声明自定义类型对象的属性或方法
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							24分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">6634人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=720&posColumn=720.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=720&posColumn=720.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="725" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/725.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=725&posColumn=725.5">
			<img src="http://a1.jikexueyuan.com/home/201504/15/c3c1/552dc3ff5a4db.jpg" class="lessonimg" title="Javascript 设计模式之代理模式" alt="Javascript 设计模式之代理模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=725&posColumn=725.5"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/725.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=725&posColumn=725.5">Javascript 设计模式之代理模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍代理模式，代理模式为其他对象提供一种代理以控制对这个对象的访问。代理模式使得代理对象控制具体对象的引用。代理几乎可以是任何对象：文件，资源，内存中的对象，或者是一些难以复制的东西。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							24分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">5581人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=725&posColumn=725.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=725&posColumn=725.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="750" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/750.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=750&posColumn=750.6">
			<img src="http://a1.jikexueyuan.com/home/201504/20/a9bf/55345b25949db.jpg" class="lessonimg" title="Javascript 设计模式之建造者模式" alt="Javascript 设计模式之建造者模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=750&posColumn=750.6"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/750.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=750&posColumn=750.6">Javascript 设计模式之建造者模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍建造者模式，建造者模式可以将一个复杂对象的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。也就是说如果我们用了建造者模式，那么用户就需要指定需要建造的类型就可以得到它们，而具体建造的过程和细节就不需要知道了。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							29分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">5451人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=750&posColumn=750.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=750&posColumn=750.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="774" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/774.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=774&posColumn=774.7">
			<img src="http://a1.jikexueyuan.com/home/201504/23/d204/553846ded6068.jpg" class="lessonimg" title="JavaScript 设计模式之命令模式" alt="JavaScript 设计模式之命令模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=774&posColumn=774.7"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/774.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=774&posColumn=774.7">JavaScript 设计模式之命令模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍命令模式，命令模式 ( Command ) 的定义是：用于将一个请求封装成一个对象，从而使你可用不同的请求对客户进行参数化；对请求排队或者记录请求日志，以及执行可撤销的操作。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							15分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">5366人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=774&posColumn=774.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=774&posColumn=774.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="822" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/822.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=822&posColumn=822.8">
			<img src="http://a1.jikexueyuan.com/home/201504/30/23f8/55418ce0a83b7.jpg" class="lessonimg" title="JavaScript 设计模式之观察者模式" alt="JavaScript 设计模式之观察者模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=822&posColumn=822.8"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/822.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=822&posColumn=822.8">JavaScript 设计模式之观察者模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍设计模式之观察者模式，观察者模式又叫发布订阅模式（Publish/Subscribe），它定义了一种一对多的关系，让多个观察者对象同时监听某一个主题对象，这个主题对象的状态发生变化时就会通知所有的观察者对象，使得它们能够自动更新自己。

		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							17分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">5856人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=822&posColumn=822.1&aCCate=javascript" >
					</a>

					<a href="http://www.jikexueyuan.com/course/model/">
						<img width="16" src="http://wirrorcdn.jikexueyuan.com/category/devbase.png" alt="model" title="设计模式" jktag="&posGP=101001&posArea=&posOper=&aCId=822&posColumn=822.2&aCCate=model" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="926" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/926.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=926&posColumn=926.9">
			<img src="http://a1.jikexueyuan.com/home/201505/21/71a5/555d394833287.jpg" class="lessonimg" title="JavaScript 设计模式之适配器模式" alt="JavaScript 设计模式之适配器模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=926&posColumn=926.9"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/926.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=926&posColumn=926.9">JavaScript 设计模式之适配器模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			适配器模式在项目开发中有着很重要的地位，比如我们开发的一些统一的接口去组合其他同学的功能就起着很关键的作用。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							18分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4690人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=926&posColumn=926.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="954" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/954.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=954&posColumn=954.10">
			<img src="http://a1.jikexueyuan.com/home/201505/26/84bc/5563d0eb94875.jpg" class="lessonimg" title="JavaScript 设计模式之职责链模式" alt="JavaScript 设计模式之职责链模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=954&posColumn=954.10"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/954.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=954&posColumn=954.10">JavaScript 设计模式之职责链模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍设计模式之职责链模式,职责链模式是使多个对象都有机会处理请求，从而避免请求的发送者和接受者之间的耦合关系。将这个对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理他为止。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							20分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4505人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=954&posColumn=954.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1390" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1390.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1390&posColumn=1390.11">
			<img src="http://a1.jikexueyuan.com/home/201506/17/572d/5580d40d9ab90.jpg" class="lessonimg" title="JavaScript 设计模式之迭代器模式" alt="JavaScript 设计模式之迭代器模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1390&posColumn=1390.11"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1390.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1390&posColumn=1390.11">JavaScript 设计模式之迭代器模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍迭代器模式,迭代器模式提供一种方法顺序访问一个聚合对象中各个元素，而又不需要暴露该方法中的内部表示。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							15分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4857人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1390&posColumn=1390.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1408" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1408.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1408&posColumn=1408.12">
			<img src="http://a1.jikexueyuan.com/home/201506/19/65d8/55836e08b7b21.png" class="lessonimg" title="JavaScript 设计模式之外观模式" alt="JavaScript 设计模式之外观模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1408&posColumn=1408.12"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1408.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1408&posColumn=1408.12">JavaScript 设计模式之外观模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍设计模式之外观模式,外观模式（Facade）为子系统中的一组接口提供了一个一致的界面，此模块定义了一个高层接口，这个接口使得这一子系统更加容易使用。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							16分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4191人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1408&posColumn=1408.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1595" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1595.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1595&posColumn=1595.13">
			<img src="http://a1.jikexueyuan.com/home/201507/15/8a29/55a5c11d411b5.jpg" class="lessonimg" title="JavaScript 设计模式之策略模式" alt="JavaScript 设计模式之策略模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1595&posColumn=1595.13"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1595.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1595&posColumn=1595.13">JavaScript 设计模式之策略模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍策略模式，策略模式定义了算法家族，分别封装起来，让他们之间可以互相替换，此模式让算法的变化不会影响到使用算法的客户。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							15分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">3846人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1595&posColumn=1595.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1617" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1617.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1617&posColumn=1617.14">
			<img src="http://a1.jikexueyuan.com/home/201605/13/f0ef/57357f7215814.jpg" class="lessonimg" title="JavaScript 设计模式之中介者模式" alt="JavaScript 设计模式之中介者模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1617&posColumn=1617.14"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1617.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1617&posColumn=1617.14">JavaScript 设计模式之中介者模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍中介者模式，中介者模式（Mediator），用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							15分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">3425人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1617&posColumn=1617.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1627" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1627.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1627&posColumn=1627.15">
			<img src="http://a1.jikexueyuan.com/home/201507/20/2ed3/55ac5b5a5a0d6.jpg" class="lessonimg" title="JavaScript 设计模式之原型模式" alt="JavaScript 设计模式之原型模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1627&posColumn=1627.15"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1627.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1627&posColumn=1627.15">JavaScript 设计模式之原型模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍原型模式，原型模式（prototype）是指用原型实例指向创建对象的种类，并且通过拷贝这些原型创建新的对象。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							33分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4996人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1627&posColumn=1627.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1658" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1658.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1658&posColumn=1658.16">
			<img src="http://a1.jikexueyuan.com/home/201507/22/fa6f/55af03c6511a8.jpg" class="lessonimg" title="JavaScript 设计模式之模板方法" alt="JavaScript 设计模式之模板方法">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1658&posColumn=1658.16"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1658.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1658&posColumn=1658.16">JavaScript 设计模式之模板方法</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍模板方法，模板方法（TemplateMethod）定义了一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							15分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4292人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1658&posColumn=1658.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1684" test="0" deg="0" >
	<div class="lessonimg-box">


		<i class="vip-icon"></i>


		<a href="http://www.jikexueyuan.com/course/1684.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1684&posColumn=1684.17">
			<img src="http://a1.jikexueyuan.com/home/201507/24/a0ce/55b19614c2358.jpg" class="lessonimg" title="JavaScript 设计模式之装饰者模式" alt="JavaScript 设计模式之装饰者模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1684&posColumn=1684.17"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1684.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1684&posColumn=1684.17">JavaScript 设计模式之装饰者模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍装饰者模式，装饰者提供比继承更有弹性的替代方案。 装饰者用用于包装同接口的对象，不仅允许你向方法添加行为，而且还可以将方法设置成原始对象调用（例如装饰者的构造函数）。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							13分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">4184人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1684&posColumn=1684.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>






<li id="1694" test="0" deg="0" >
	<div class="lessonimg-box">



		<i class="rz-icon"></i>

		<a href="http://www.jikexueyuan.com/course/1694.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1694&posColumn=1694.18">
			<img src="http://a1.jikexueyuan.com/home/201507/27/294d/55b5919e9c7a3.jpg" class="lessonimg" title="JavaScript 设计模式之组合模式" alt="JavaScript 设计模式之组合模式">

			<div class="lessonplay" style="opacity: 0;">
				<i class="playericon" jktag="&posGP=103001&posArea=&posOper=&aCId=1694&posColumn=1694.18"></i>
			</div>


		</a>

	</div>

	<div class="lesson-infor" style="height: 88px;">
		<h2 class="lesson-info-h2"><a href="http://www.jikexueyuan.com/course/1694.html" target="_blank" jktag="&posGP=103001&posArea=&posOper=&aCId=1694&posColumn=1694.18">JavaScript 设计模式之组合模式</a></h2>
		<p style="height: 0px; opacity: 0; display: none;">
			本课程介绍组合模式，组合模式（Composite）将对象组合成树形结构以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性。
		</p>
		<div class="timeandicon">
			<div class="cf">
				<dl>
					<dd class="mar-b8"><i class="time-icon"></i><em>4课时
							13分钟</em>
					</dd>
					<dd class="zhongji">

					<i class="xinhao-icon3"></i><em>高级</em>
					</dd>

				</dl>
				<em class="learn-number">5086人学习</em>
			</div>
			<div class="cf">
				<div class="lessonicon-box">

					<a href="http://www.jikexueyuan.com/course/javascript/">
						<img width="16" src="http://a1.jikexueyuan.com/home/201606/12/69f4/575cbb2ff238d.png" alt="javascript" title="JavaScript" jktag="&posGP=101001&posArea=&posOper=&aCId=1694&posColumn=1694.1&aCCate=javascript" >
					</a>

				</div>
			</div>
		</div>
	</div>
</li>




					</ul>
				</div>
				<div class="stage-more" index ="total_7">
					<!--查看更多课程 <img src="/static/images/more.png"/>-->
					<div style="width:100px;height:40px; margin:0 auto">查看更多课程 <img src="http://s1.jikexueyuan.com/path/images/more_3b4d448.png" style="
    float: right;
    margin-top: 18px;
"></div>
				</div>
			</div>

			<div class="page-oneicon ">
				<img src="http://s1.jikexueyuan.com/path/images/next_eaadfa6.png" />
			</div>
		</div>
		<!--pathstage end-->

			<div class="over" style="display: none;">不断完善中</div>
		</div>

	</div>
</div>
<script>
	// 埋点统计需要 将 slug打到全局变量
	window.pathSlug = 'javascript';
</script>






            </div>

<div id="footer" class="mar-t50">
	<link rel="stylesheet" href="http://e.jikexueyuan.com/headerandfooter/css/footer.css" />
	<div class=" jkinfor-block">
		<div class="jkinfor cf">
			<div class="jk-logo">
				<img src="http://e.jikexueyuan.com/headerandfooter/images/jk-logo-footer.png">
				<p>极客学院，编程是一种信仰！</p>
			</div>
			<dl>
				<dt>职业学院</dt>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/zhiye/web">Web前端工程师</a></dd>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/zhiye/python">Python Web工程师</a></dd>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/zhiye/go">Go语言工程师</a></dd>
				<!--<dd><a target="_blank" href="http://j.jikexueyuan.com/train/android?huodong=jiuye_android_in">Android学院</a></dd>-->
				<dd><a target="_blank" href="http://www.jikexueyuan.com/zhiye/ios">iOS工程师</a></dd>
			</dl>
			<dl>
				<dt>会员课程</dt>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/course/">课程库</a></dd>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/path/">知识体系图</a></dd>
				<dd><a target="_blank" href="http://ke.jikexueyuan.com/zhiye/">职业路径图</a></dd>
				<dd><a target="_blank" href="http://ke.jikexueyuan.com/xilie/">系列课程</a></dd>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/tag/">课程标签</a></dd>
			</dl>
			<dl>
				<dt>极客社区</dt>
				<dd><a target="_blank" href="http://wenda.jikexueyuan.com/">技术问答</a></dd>
				<dd><a target="_blank" href="http://wiki.jikexueyuan.com/">Wiki</a></dd>
				<dd><a target="_blank" href="http://download.jikexueyuan.com/">资源下载</a></dd>
				<dd><a target="_blank" href="http://qun.jikexueyuan.com/">社群</a></dd>
			</dl>
			<dl>
				<dt>其他</dt>
				<dd><a target="_blank" href="http://help.jikexueyuan.com/">关于我们</a></dd>
				<dd><a target="_blank" href="http://help.jikexueyuan.com/guide/">使用指南</a></dd>
				<dd><a target="_blank" href="http://help.jikexueyuan.com/join.html">加入我们</a></dd>
				<dd><a target="_blank" href="http://help.jikexueyuan.com/contact.html">联系我们</a></dd>
				<dd><a target="_blank" href="http://www.jikexueyuan.com/friendlink.html">友情链接</a></dd>
			</dl>

			<div class="jk-down">
				<p class="hot-tel">服务热线:400-678-8266</p>
				<div class="downCon down-ios">
					<img src="http://e.jikexueyuan.com/headerandfooter/images/app.png" class="twoCode" alt="下载二维码"> iPhone
				</div>
				<div class="downCon down-and">
					<img src="http://e.jikexueyuan.com/headerandfooter/images/app.png" class="twoCode" alt="下载二维码"> Android
				</div>
			</div>
		</div>

	</div>
	<div class="w-1000 copyright">
		Copyright © 2013-2016&nbsp;<strong><a href="http://www.jikexueyuan.com/" target="_blank">jikexueyuan.com</a></strong> All Rights Reversed. 京ICP备11018032号-8 京公网安备11010802020210
		<a href="http://qun.jikexueyuan.com/jikexueyuan/topic/430" target="_blank" class="down-wechat"></a>
		<a href="http://weibo.com/jikexueyuan" target="_blank" class="down-sina"></a>
	</div>
</div>

<div class="gotop" id="gototop">
	<span class="top" style="display: block;"></span>
	<span class="erwma" style="display:none">
		<img src="http://e.jikexueyuan.com/headerandfooter/images/erwma.png" style="display: none;">
	</span>
	<a href="http://www.jikexueyuan.com/app" alt="极客学院应用" target="_blank">
		<span class="jk-app"><div class="appewm"></div></span>
	</a>
	<a href="javascript:;" id="diaochaid" class="diaocha"></a>
	<a onclick="doyoo.util.openChat('g=10059996');return false;" href="javascript:;" class="apply qq-online qq-online1" rel="nofollow"><span class="kefu">在线客服<br>  工作日9:00-21:00在线<i></i></span></a>
</div>
<script src="http://e.jikexueyuan.com/headerandfooter/js/footer.min.js"></script>
<script type="text/javascript" charset="utf-8" src="http://lead.soperson.com/20001269/10057537.js"></script>
<script type="text/javascript" src="http://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">
	BAIDU_CLB_fillSlotAsync('2478912', 'diaochaid');
</script>


        </div>
         <script type="text/javascript">LazyLoad=function(e){function t(t,n){var s,r=e.createElement(t);for(s in n)n.hasOwnProperty(s)&&r.setAttribute(s,n[s]);return r}function n(e){var t,n,s=i[e];s&&(t=s.callback,n=s.urls,n.shift(),u=0,n.length||(t&&t.call(s.context,s.obj),i[e]=null,f[e].length&&r(e)))}function s(){var t=navigator.userAgent;o={async:e.createElement("script").async===!0},(o.webkit=/AppleWebKit\//.test(t))||(o.ie=/MSIE|Trident/.test(t))||(o.opera=/Opera/.test(t))||(o.gecko=/Gecko\//.test(t))||(o.unknown=!0)}function r(r,u,h,g,d){var p,y,m,b,k,v,j=function(){n(r)},w="css"===r,E=[];if(o||s(),u)if(u="string"==typeof u?[u]:u.concat(),w||o.async||o.gecko||o.opera)f[r].push({urls:u,callback:h,obj:g,context:d});else for(p=0,y=u.length;y>p;++p)f[r].push({urls:[u[p]],callback:p===y-1?h:null,obj:g,context:d});if(!i[r]&&(b=i[r]=f[r].shift())){for(l||(l=e.head||e.getElementsByTagName("head")[0]),k=b.urls,p=0,y=k.length;y>p;++p){if(v=k[p],w?m=o.gecko?t("style"):t("link",{href:v,rel:"stylesheet"}):(m=t("script",{src:v}),m.async=!1),m.className="lazyload",m.setAttribute("charset","utf-8"),o.ie&&!w&&"onreadystatechange"in m&&!("draggable"in m))m.onreadystatechange=function(){/loaded|complete/.test(m.readyState)&&(m.onreadystatechange=null,j())};else if(w&&(o.gecko||o.webkit))if(o.webkit){var T;if(b.urls[p]=m.href,T=c()){p--,y=k.length;continue}}else m.innerHTML='@import "'+v+'";',a(m);else m.onload=m.onerror=j;E.push(m)}var A=document.createDocumentFragment();for(p=0,y=E.length;y>p;++p)A.appendChild(E[p]);var x;return"css"===r?x=l:"js"===r&&(x=document.getElementById("pages-container")||l),x.appendChild(A),E}}function a(e){var t;try{t=!!e.sheet.cssRules}catch(s){return u+=1,void(200>u?setTimeout(function(){a(e)},50):t&&n("css"))}n("css")}function c(){var e,t=i.css,s=!1;if(t){for(e=h.length;--e>=0;)if(h[e].href===t.urls[0]){s=!0,n("css");break}u+=1,t&&(200>u?setTimeout(c,50):n("css"))}return s}var o,l,i={},u=0,f={css:[],js:[]},h=e.styleSheets;return{css:function(e,t,n,s){r("css",e,t,n,s)},js:function(e,t,n,s){r("js",e,t,n,s)}}}(this.document);</script>
       	<script type="text/javascript" src="http://sp1.jikexueyuan.com/static/scripts/LoginAndRegister.js"></script>
     <script type="text/javascript">var _ready = false;_list = [];_when = function(cb) {_ready?cb():_list.push(cb);};LazyLoad.js(['http://s1.jikexueyuan.com/common/js/TweenMax.min_5a7da72.js', 'http://s1.jikexueyuan.com/common/pkg/common_sync0_libs_1a4ebbf.js', 'http://s1.jikexueyuan.com/common/js/setcookie_51991d5.js', 'http://s1.jikexueyuan.com/common/js/swfobject_5fb5452.js', 'http://s1.jikexueyuan.com/common/pkg/common_sync1_libs_cf97d43.js', 'http://s1.jikexueyuan.com/common/widget/loading/loading_197f16e.js', 'http://s1.jikexueyuan.com/path/widget/lessoninfor/lessoninfor_dcb7662.js'], function () {!function() {
		require("common:widget/loading/loading.js").init();
		$('.pathdescibe,.pathstage,.over').fadeIn();
	}();
!function() { require("path:widget/lessoninfor/lessoninfor.js").init(); }();;_ready=true;var _item; while((_item=_list.shift())){_item();}});</script></body>
</html>
'''

selector = etree.HTML(html)
# 提取文本

urlsharepart = '//div[@id="wrapper"]/div[@id="pager"]/div[@id="container"]/div[@class="wrap w-1000"]/div[@class="pathstage mar-t30"]'
urlmodulepart = 'div[@class="pathstage-txt"]/h2/text()'
urllessonnamesharepart = 'div[@class="stagebox "]/div[@class="stagewidth lesson-list"]/ul/li/div[@class="lesson-infor"]/h2'
urllessonname = 'a/text()'
urllessonurl = 'a/@href'
urlshare = selector.xpath(urlsharepart)

urllessonshare_list = []
lesson_url_dict = {}
module_lesson_dict = {}

def createfolder():
    obtainsubfoldername_dict = obtainsubfoldername(urllessonshare, urllessonname, urllessonurl, moduleseq, modulename)
    subfoldername = obtainsubfoldername_dict[0]
    for folder in subfoldername:
        os.mkdir(folder)

lesson_url_list_a = []
lesson_url_list_b = []
lesson_url_list = []

def obtain_url():
    obtainsubfoldername_dict = obtainsubfoldername(urllessonshare, urllessonname, urllessonurl, moduleseq, modulename)
    for x in obtainsubfoldername_dict[1].items():
        url_list = x[1]
        for y in url_list.items():
            url = y[1]
            lesson_url_list_a.append(url)
        # lesson_url_list_b.extend(lesson_url_list_a)
    # print(lesson_url_list_b)
    return lesson_url_list_a

for eachurlshare in urlshare:
    urlmodule = eachurlshare.xpath(urlmodulepart)[0]
    if urlmodule[1] in range(10):
        # for equal or large than 10
        moduleseq = urlmodule[0:2]
        modulename = urlmodule[4:]  ###
    else:
        # for less than 10
        moduleseq = urlmodule[0]
        modulename = urlmodule[3:]  ###
    urllessonshare = eachurlshare.xpath(urllessonnamesharepart)

    # createfolder()
    lesson_url_list_a = obtain_url()
    # print(lesson_url_list_a)
    # print(lesson_url_list)
    # lesson_url_list.extend(lesson_url_list_a)
    # lesson_url_list.extend(a())
    # import itertools
    # list(itertools.chain.from_iterable(lesson_url_list))

def final_obtain_url():
    print(lesson_url_list_a)
    return lesson_url_list_a

'''
lessonname1 = selector.xpath(urlsharepart + urllessonname1)
for eachlessonname1 in lessonname1:
    print (eachlessonname1)
'''

# module = selector.xpath('//div[@id="wrapper"]/div[@id="pager"]/div[@id="container"]/div[@class="wrap w-1000"]')
# title = .extract().replace(' ', '')

''' 1. Course = Python
    2. Module
    3. Lesson
'''

# if __name__ == "__main__":
#     createfolder()