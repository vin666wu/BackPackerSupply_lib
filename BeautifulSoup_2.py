{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOPdsaQ2Tnzd/fDE+YNfhmC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vin666wu/BackPackerSupply_lib/blob/master/BeautifulSoup_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QEepnH4a7yE-"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url ='https://water.taiwanstat.com/'\n",
        "web = requests.get(url)\n",
        "soup = BeautifulSoup(web.text, \"html.parser\")\n",
        "reservoir = soup.select('.reservoir') # 取得所有 class 為 reservoir 的 tag\n",
        "# print(soup)\n",
        "for i in reservoir:\n",
        "  print(i.find('div', class_ = 'name').get_text(), end=' ')  # 取得內容的 class 為 name 的 div 文字\n",
        "  print(i.find('h5').get_text(),end= ' ') # 取得內容 h5 tag 的文字\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ApqDxBk67-i9",
        "outputId": "711cde1b-9556-4703-a9e3-31898c7ce7ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<!DOCTYPE html>\n",
            "<html lang=\"zh-TW\" xmlns=\"http://www.w3.org/1999/xhtml\"><head><meta content=\"台灣水庫即時水情\" property=\"og:title\"/><meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/><meta content=\"台灣水庫即時水情\" property=\"og:site_name\"/><meta content=\"台灣水庫即時水情-視覺化, 即時蓄水量、水位變化...\" property=\"og:description\"/><meta content=\"http://i.imgur.com/04AFcnA.png\" property=\"og:image\"/><meta content=\"image/png\" property=\"og:image:type\"/><meta content=\"Chi-Hsuan Huang\" name=\"author\"/><meta content=\"Po-An Yang\" name=\"citation_authors\"/><meta content=\"台灣水庫即時水情-視覺化, 即時蓄水量、水位變化\" name=\"description\"/><title>台灣水庫即時水情</title><meta content=\"zh_TW\" property=\"og:locale\"/><meta content=\"width=device-width,initial-scale=1\" name=\"viewport\"/><link href=\"//static.taiwanstat.com/favicon.ico\" rel=\"icon\" type=\"image/png\"/><link href=\"//static.taiwanstat.com/favicon.ico\" rel=\"shortcut icon\" type=\"image/x-icon\"/><link href=\"//static.taiwanstat.com/css/style.min.css\" rel=\"stylesheet\"/><link href=\"//storage.googleapis.com/code.getmdl.io/1.0.6/material.amber-orange.min.css\" rel=\"stylesheet\"/><link href=\"//static.taiwanstat.com/bower_components/semantic/dist/semantic.min.css\" rel=\"stylesheet\"/><link href=\"./css/main.css\" media=\"all\" rel=\"stylesheet\" type=\"text/css\"/><link href=\"css/style.css\" rel=\"stylesheet\" type=\"text/css\"/> <script async=\"\" src=\"//storage.googleapis.com/code.getmdl.io/1.0.6/material.min.js\"></script> <link href=\"https://fonts.googleapis.com/icon?family=Material+Icons\" rel=\"stylesheet\"/></head><body><div class=\"mdl-layout mdl-js-layout mdl-layout--fixed-header\" id=\"layout-header\"> <header class=\"mdl-layout__header\"><div class=\"mdl-layout__header-row\"><span class=\"mdl-layout-title\"><a href=\"https://www.taiwanstat.com/realtime/\"><img alt=\"logo\" class=\"round-logo\" src=\"https://static.taiwanstat.com/realtime/images/assert/round-logo.png\"/>用數據看台灣</a></span><div class=\"mdl-layout-spacer\"></div> <nav class=\"mdl-navigation mdl-layout--large-screen-only\"><a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/realtime/\">台灣開放即時資料</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/statistics/\">台灣開放統計資料</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/global/r/\">世界即時資訊</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/global/l/\">世界統計資訊</a> <a class=\"mdl-navigation__link\" href=\"https://taiwanstat.com/blog/opendata/\">開放資料分析部落格</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/about/\">關於我們</a></nav><div></div></div> </header><div class=\"mdl-layout__drawer\"><span class=\"mdl-layout-title\"><a href=\"https://www.taiwanstat.com/realtime/\"><img alt=\"logo\" class=\"round-logo\" src=\"https://static.taiwanstat.com/realtime/images/assert/round-logo.png\"/>用數據看台灣</a></span> <nav class=\"mdl-navigation\"><a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/realtime/\">台灣開放即時資料</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/statistics/\">台灣開放統計資料</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/global/r/\">世界即時資訊</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/global/l/\">世界統計資訊</a> <a class=\"mdl-navigation__link\" href=\"https://taiwanstat.com/blog/opendata/\">開放資料分析部落格</a> <a class=\"mdl-navigation__link\" href=\"https://www.taiwanstat.com/about/\">關於我們</a></nav></div> <main class=\"mdl-layout__content\" id=\"main-content\"><div class=\"main\"><div class=\"title__wrapper\"><h1 id=\"title\">台灣水庫即時水情</h1><div class=\"fb-plugin\"><div class=\"fb-like\" data-action=\"like\" data-href=\"http://water.taiwanstat.com/\" data-layout=\"standard\" data-share=\"true\" data-show-faces=\"true\" data-width=\"300px\"></div></div></div><div class=\"links\"> <button class=\"go-to\" onclick=\"window.location.href='#reservoir1'\">北部</button> <button class=\"go-to\" onclick=\"window.location.href='#reservoir6'\">中部</button> <button class=\"go-to\" onclick=\"window.location.href='#reservoir12'\">南部</button></div><ul class=\"note sml-hide\"><li class=\"data-src\">資料來源：<a href=\"http://www.wra.gov.tw/\">經濟部水利署</a></li><li>即時水情資料係自記儀器自動產生，未經人工完整檢驗，僅提供參考。</li><li>根據<a href=\"http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx\">水利署網頁</a>公布，各項水庫資料由各水庫管理單位在每日輸入，更新時間不一致。（部分水庫星期六、日之資料則在星期一統一輸入）</li><li class=\"red\">預測剩餘天數 = 即時有效蓄水量/昨日下降蓄水量。因降雨、用水量隨時間變化，預測結果僅提供參考。</li></ul><div class=\"reservoir-wrap\"><div class=\"reservoir\"><div class=\"name\"><h3>新山水庫(基隆)</h3></div> <svg height=\"250\" id=\"reservoir0\" width=\"100%\"></svg><div class=\"volumn\"><h5>7001.1萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>翡翠水庫(台北、新北)</h3></div> <svg height=\"250\" id=\"reservoir1\" width=\"100%\"></svg><div class=\"volumn\"><h5>26722.51萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>石門水庫(新北、桃園、新竹)</h3></div> <svg height=\"250\" id=\"reservoir2\" width=\"100%\"></svg><div class=\"volumn\"><h5>4025.63萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>永和山水庫(新竹、苗栗)</h3></div> <svg height=\"250\" id=\"reservoir3\" width=\"100%\"></svg><div class=\"volumn\"><h5>685.598萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>寶山水庫(新竹)</h3></div> <svg height=\"250\" id=\"reservoir20\" width=\"100%\"></svg><div class=\"volumn\"><h5>7001.1萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>寶山第二水庫(新竹)</h3></div> <svg height=\"250\" id=\"reservoir4\" width=\"100%\"></svg><div class=\"volumn\"><h5>7001.1萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>明德水庫(苗栗)</h3></div> <svg height=\"250\" id=\"reservoir5\" width=\"100%\"></svg><div class=\"volumn\"><h5>262.0316萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>鯉魚潭水庫(苗栗、台中)</h3></div> <svg height=\"250\" id=\"reservoir6\" width=\"100%\"></svg><div class=\"volumn\"><h5>9857.34萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>德基水庫(台中)</h3></div> <svg height=\"250\" id=\"reservoir7\" width=\"100%\"></svg><div class=\"volumn\"><h5>762.27萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>石岡壩(台中)</h3></div> <svg height=\"250\" id=\"reservoir8\" width=\"100%\"></svg><div class=\"volumn\"><h5>11486萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>日月潭水庫(南投)</h3></div> <svg height=\"250\" id=\"reservoir9\" width=\"100%\"></svg><div class=\"volumn\"><h5>5741萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>霧社水庫(南投)</h3></div> <svg height=\"250\" id=\"reservoir10\" width=\"100%\"></svg><div class=\"volumn\"><h5>3269.4萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>湖山水庫(雲林、彰化、嘉義)</h3></div> <svg height=\"250\" id=\"reservoir19\" width=\"100%\"></svg><div class=\"volumn\"><h5>820.884613萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>仁義潭水庫(嘉義)</h3></div> <svg height=\"250\" id=\"reservoir12\" width=\"100%\"></svg><div class=\"volumn\"><h5>820.884613萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>蘭潭水庫(嘉義)</h3></div> <svg height=\"250\" id=\"reservoir21\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>白河水庫(台南)</h3></div> <svg height=\"250\" id=\"reservoir13\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>曾文水庫(嘉義、台南)</h3></div> <svg height=\"250\" id=\"reservoir14\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>烏山頭水庫(台南)</h3></div> <svg height=\"250\" id=\"reservoir15\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>南化水庫(台南、高雄)</h3></div> <svg height=\"250\" id=\"reservoir16\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>阿公店水庫(高雄)</h3></div> <svg height=\"250\" id=\"reservoir17\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div><div class=\"reservoir\"><div class=\"name\"><h3>牡丹水庫(屏東)</h3></div> <svg height=\"250\" id=\"reservoir18\" width=\"100%\"></svg><div class=\"volumn\"><h5>1086.97萬立方公尺</h5></div><div class=\"state\"><h5>萬立方公尺</h5></div><div class=\"updateAt\">更新時間：0000-00-00 (0時)</div></div></div></div><div class=\"mdl-card mdl-shadow--2dp author\"><h4><a href=\"http://taiwanstat_members.cannerapp.com/\">About Author</a></h4> <img alt=\"logo\" class=\"ui circular image\" src=\"https://static.taiwanstat.com/realtime/images/assert/round-logo.png\"/><div class=\"author-info\"><h5>Chi-Hsuan Huang</h5></div></div><div class=\"license__wrapper\">\n",
            "<a href=\"http://creativecommons.org/licenses/by-nc-sa/4.0/\" rel=\"license\">\n",
            "<img alt=\"創用 CC 授權條款\" src=\"https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png\" style=\"border-width:0\"/></a><br/>本著作由<a href=\"http://www.taiwanstat.com\" property=\"cc:attributionName\" rel=\"cc:attributionURL\" xmlns:cc=\"http://creativecommons.org/ns#\">用數據看台灣團隊</a>製作，以<a href=\"http://creativecommons.org/licenses/by-nc-sa/4.0/\" rel=\"license\">創用CC 姓名標示-非商業性-相同方式分享 4.0 國際 授權條款</a>釋出。\n",
            "</div></main></div><div class=\"footer-mobile\"> <button class=\"scrollup mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored mdl-shadow--2dp\" id=\"set\"><i class=\"material-icons\">keyboard_arrow_up</i></button></div> <footer class=\"mdl-mini-footer\"><div class=\"mdl-mini-footer__left-section\">©2021 <a href=\"https://www.taiwanstat.com/about/\">用數據看台灣</a>· <a href=\"https://www.facebook.com/taiwanstat/?fref=ts\"><i class=\"facebook square icon\"></i></a> · <a href=\"https://github.com/TaiwanStat\"><i class=\"github square icon\"></i></a></div><div class=\"mdl-mini-footer__right-section\"><span class=\"footer_msg\"><a href=\"https://www.buymeacoffee.com/taiwanstat\">歡迎贊助我們一杯咖啡！</a>意見回饋 </span>歡迎來信: <a href=\"mailto:service@taiwanstat.com\">service@taiwanstat.com</a></div> </footer><div id=\"fb-root\"></div> <script src=\"//cdnjs.cloudflare.com/ajax/libs/d3/3.5.9/d3.min.js\"></script> <script src=\"//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script> <script src=\"js/liquidFillGauge.js\"></script> <script src=\"js/index.js\"></script> <script>!function(e,a,t,n,c,o,s){e.GoogleAnalyticsObject=c,e[c]=e[c]||function(){(e[c].q=e[c].q||[]).push(arguments)},e[c].l=1*new Date,o=a.createElement(t),s=a.getElementsByTagName(t)[0],o.async=1,o.src=n,s.parentNode.insertBefore(o,s)}(window,document,\"script\",\"//www.google-analytics.com/analytics.js\",\"ga\"),ga(\"create\",\"UA-61023469-1\",\"auto\"),ga(\"send\",\"pageview\")</script> <script>!function(e,t,n){var o,c=e.getElementsByTagName(t)[0];e.getElementById(n)||(o=e.createElement(t),o.id=n,o.src=\"//connect.facebook.net/zh_TW/sdk.js#xfbml=1&version=v2.5\",c.parentNode.insertBefore(o,c))}(document,\"script\",\"facebook-jssdk\")</script> <script src=\"//static.taiwanstat.com/js/main.min.js\"></script> </body></html>\n",
            "新山水庫(基隆) 7001.1萬立方公尺 \n",
            "翡翠水庫(台北、新北) 26722.51萬立方公尺 \n",
            "石門水庫(新北、桃園、新竹) 4025.63萬立方公尺 \n",
            "永和山水庫(新竹、苗栗) 685.598萬立方公尺 \n",
            "寶山水庫(新竹) 7001.1萬立方公尺 \n",
            "寶山第二水庫(新竹) 7001.1萬立方公尺 \n",
            "明德水庫(苗栗) 262.0316萬立方公尺 \n",
            "鯉魚潭水庫(苗栗、台中) 9857.34萬立方公尺 \n",
            "德基水庫(台中) 762.27萬立方公尺 \n",
            "石岡壩(台中) 11486萬立方公尺 \n",
            "日月潭水庫(南投) 5741萬立方公尺 \n",
            "霧社水庫(南投) 3269.4萬立方公尺 \n",
            "湖山水庫(雲林、彰化、嘉義) 820.884613萬立方公尺 \n",
            "仁義潭水庫(嘉義) 820.884613萬立方公尺 \n",
            "蘭潭水庫(嘉義) 1086.97萬立方公尺 \n",
            "白河水庫(台南) 1086.97萬立方公尺 \n",
            "曾文水庫(嘉義、台南) 1086.97萬立方公尺 \n",
            "烏山頭水庫(台南) 1086.97萬立方公尺 \n",
            "南化水庫(台南、高雄) 1086.97萬立方公尺 \n",
            "阿公店水庫(高雄) 1086.97萬立方公尺 \n",
            "牡丹水庫(屏東) 1086.97萬立方公尺 \n"
          ]
        }
      ]
    }
  ]
}