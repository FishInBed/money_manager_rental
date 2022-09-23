def default_flex_template():
  contents = {
     "type": "bubble",
     "size": "mega",
     "hero": {
              "type": "image",
              "url": "https://i-ogp.pximg.net/c/540x540_70/img-master/img/2011/12/07/19/34/15/23516160_p0_square1200.jpg",
              "size": "full",
              "aspectRatio": "20:20",
              "aspectMode": "cover"
             },
     "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                           {
                            "type": "text",
                            "weight": "regular",
                            "size": "md",
                            "margin": "none",
                            "contents": [
                                         {
                                          "type": "span",
                                          "text": "嗨我是錢錢管家🤵"
                                         }
                                        ],
                            "position": "relative",
                            "align": "center",
                            "wrap": True
                            },
                            {
                             "type": "text",
                             "weight": "regular",
                             "size": "md",
                             "margin": "sm",
                             "contents": [
                                          {
                                           "type": "span",
                                           "text": "召喚我有什麼事嗎👀\n第一次使用建議先點選「管家的打開方式」喔~",
                                          }
                                         ],
                            "position": "relative",
                            "wrap": True,
                            "align": "center"
                            },
                            {
                             "type": "box",
                             "layout": "vertical",
                             "contents": [
                                          {
                                           "type": "separator",
                                           "margin": "lg",
                                           "color": "#4f2f56"
                                          }
                                         ]
                            }
                           ]
             },
     "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "xs",
                "contents": [
                             {
                              "type": "button",
                              "style": "link",
                              "height": "sm",
                              "action": {
                                         "type": "postback",
                                         "label": "我決定雇用你了👊",
                                         "data": "new_group_member",
                                         "displayText": "我決定雇用你了"
                                        },
                              "margin": "none",
                              "color": "#990000",
                              "wrap": True
                             },
                             {
                              "type": "button",
                              "action": {
                                         "type": "postback",
                                         "label": "管家的打開方式📖",
                                         "data": "call_manual",
                                         "displayText": "管家的打開方式"
                                        },
                              "color": "#990000",
                              "style": "link",
                              "height": "sm",
                              "margin": "none"
                             },
                             {
                              "type": "button",
                              "style": "link",
                              "height": "sm",
                              "action": {
                                         "type": "postback",
                                         "label": "幫我記個帳💰",
                                         "data": "insert_group_data",
                                         "displayText": "幫我記個帳"
                                        },
                              "color": "#990000",
                              "margin": "none"
                             },
                             {
                              "type": "button",
                              "style": "link",
                              "height": "sm",
                              "action": {
                                         "type": "postback",
                                         "label": "幫我們算個帳💸",
                                         "data": "calculate_money",
                                         "displayText": "幫我們算個帳"
                                        },
                              "color": "#990000",
                              "margin": "none"
                             }
                            ],
                "flex": 0,
                "offsetTop": "none",
                "offsetStart": "none",
                "offsetBottom": "none",
                "offsetEnd": "none",
                "paddingAll": "xs",
                "paddingTop": "none",
                "paddingBottom": "lg",
                "backgroundColor": "#ffdfff",
                "borderWidth": "none"
               },
     "styles": {
                "body": {
                         "separator": True,
                         "backgroundColor": "#ffdfff",
                         "separatorColor": "#694d80"
                        }
               }
    }
  return contents

def old_flex_template():
  contents = {
     "type": "bubble",
     "size": "mega",
     "hero": {
              "type": "image",
              "url": "https://i-ogp.pximg.net/c/540x540_70/img-master/img/2011/12/07/19/34/15/23516160_p0_square1200.jpg",
              "size": "full",
              "aspectRatio": "20:20",
              "aspectMode": "cover"
             },
     "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                           {
                            "type": "text",
                            "weight": "regular",
                            "size": "md",
                            "margin": "none",
                            "contents": [
                                         {
                                          "type": "span",
                                          "text": "嗨我是你的錢錢管家🤵"
                                         }
                                        ],
                            "position": "relative",
                            "align": "center"
                            },
                            {
                             "type": "text",
                             "weight": "regular",
                             "size": "md",
                             "margin": "sm",
                             "contents": [
                                          {
                                           "type": "span",
                                           "text": "召喚我有什麼事嗎👀"
                                          }
                                         ],
                            "position": "relative",
                            "align": "center"
                            },
                            {
                             "type": "box",
                             "layout": "vertical",
                             "contents": [
                                          {
                                           "type": "separator",
                                           "margin": "lg",
                                           "color": "#4f2f56"
                                          }
                                         ]
                            }
                           ]
             },
     "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "xs",
                "contents": [
                             {
                              "type": "button",
                              "action": {
                                         "type": "postback",
                                         "label": "管家的打開方式📖",
                                         "data": "call_manual",
                                         "displayText": "管家的打開方式"
                                        },
                              "color": "#990000",
                              "style": "link",
                              "height": "sm",
                              "margin": "none"
                             },
                             {
                              "type": "button",
                              "style": "link",
                              "height": "sm",
                              "action": {
                                         "type": "postback",
                                         "label": "幫我記個帳💰",
                                         "data": "insert_group_data",
                                         "displayText": "幫我記個帳"
                                        },
                              "color": "#990000",
                              "margin": "none"
                             },
                             {
                              "type": "button",
                              "style": "link",
                              "height": "sm",
                              "action": {
                                         "type": "postback",
                                         "label": "幫我們算個帳💸",
                                         "data": "calculate_money",
                                         "displayText": "幫我們算個帳"
                                        },
                              "color": "#990000",
                              "margin": "none"
                             }
                            ],
                "flex": 0,
                "offsetTop": "none",
                "offsetStart": "none",
                "offsetBottom": "none",
                "offsetEnd": "none",
                "paddingAll": "xs",
                "paddingTop": "none",
                "paddingBottom": "lg",
                "backgroundColor": "#ffdfff",
                "borderWidth": "none"
               },
     "styles": {
                "body": {
                         "separator": True,
                         "backgroundColor": "#ffdfff",
                         "separatorColor": "#694d80"
                        }
               }
    }
  return contents

def manual():
  contents = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "💾錢錢管家的使用說明書💾",
            "size": "lg",
            "align": "center",
            "offsetEnd": "none",
            "offsetBottom": "md"
          },
          {
            "type": "text",
            "text": "哈囉我是錢錢管家🧚‍♀️\n一個幫助合租好室友們記帳的家事小精靈\n如果你想僱用我幫忙記帳的話，請輸入\n「我決定雇用你了」或是點選上面的按鈕\n記得一定要大家都雇用我，在計算的時候才不會出錯喔\n想要召喚我出來的話有旁邊兩種方式",
            "wrap": True,
            "size": "sm",
            "offsetTop": "md",
            "align": "start"
          },
          {
            "type": "text",
            "offsetTop": "xl",
            "align": "center",
            "offsetBottom": "xl",
            "contents": [
              {
                "type": "span",
                "text": "➡➡➡➡➡➡➡➡➡➡➡➡➡➡",
                "size": "md",
                "color": "#e4c53f"
              }
            ],
            "margin": "none"
          }
        ],
        "offsetBottom": "none",
        "offsetTop": "none",
        "justifyContent": "center",
        "backgroundColor": "#fefecd",
        "borderWidth": "none",
        "borderColor": "#fefecd"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "offsetBottom": "md",
        "backgroundColor": "#fefecd",
        "borderColor": "#fefecd"
      }
    },
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "💾錢錢管家的使用說明書💾",
            "size": "lg",
            "align": "center"
          }
        ],
        "backgroundColor": "#fefecd"
      },
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "1️⃣ 極簡模式",
            "size": "md",
            "align": "center"
          }
        ]
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "🧐"
          },
          {
            "type": "text",
            "text": "只要打出",
            "wrap": True,
            "size": "sm",
            "margin": "none",
            "offsetBottom": "sm",
            "offsetTop": "none"
          },
          {
            "type": "separator"
          },
          {
            "type": "text",
            "text": "召喚錢錢管家記一下\n品項 價錢 日期",
            "size": "sm",
            "margin": "sm",
            "wrap": True,
            "offsetBottom": "sm",
            "offsetTop": "none",
            "weight": "bold"
          },
          {
            "type": "separator"
          },
          {
            "type": "text",
            "text": "我就會出來幫您記帳喔\n示範一下：",
            "margin": "none",
            "size": "sm",
            "offsetTop": "sm",
            "offsetBottom": "sm",
            "wrap": True
          },
          {
            "type": "text",
            "text": "召喚錢錢管家記一下\n水費 900 2022-08-09\n電費 950 2022-08-19",
            "offsetTop": "md",
            "size": "sm",
            "wrap": True,
            "style": "italic",
            "color": "#000079",
            "offsetBottom": "xs"
          },
          {
            "type": "text",
            "text": "出現恭喜訊息就表示記帳成功",
            "margin": "lg",
            "size": "sm",
            "offsetBottom": "md",
            "offsetTop": "none"
          },
          {
            "type": "text",
            "text": "🧐",
            "offsetTop": "md",
            "offsetBottom": "md"
          },
          {
            "type": "text",
            "text": "只要打出",
            "offsetTop": "md",
            "size": "sm",
            "offsetBottom": "md"
          },
          {
            "type": "separator",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "召喚錢錢管家算一下\n想要結算的年份-想要結算的月份",
            "size": "sm",
            "margin": "sm",
            "wrap": True,
            "offsetBottom": "sm",
            "offsetTop": "none",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "sm"
          },
          {
            "type": "text",
            "text": "我就會幫您結算那個月分大家各要收到或是再付多少錢喔\n示範一下：",
            "margin": "none",
            "size": "sm",
            "offsetTop": "sm",
            "offsetBottom": "sm",
            "wrap": True
          },
          {
            "type": "text",
            "text": "召喚錢錢管家算一下\n2022-08",
            "offsetTop": "md",
            "size": "sm",
            "wrap": True,
            "style": "italic",
            "color": "#000079",
            "offsetBottom": "xs"
          }
        ]
      },
      "styles": {
        "header": {
          "backgroundColor": "#fefecd"
        },
        "hero": {
          "backgroundColor": "#fefecd"
        },
        "body": {
          "backgroundColor": "#fefecd"
        }
      }
    },
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "💾錢錢管家的使用說明書💾",
            "size": "lg",
            "align": "center"
          }
        ],
        "backgroundColor": "#fefecd"
      },
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "2️⃣ 抬槓模式",
            "size": "md",
            "align": "center"
          }
        ]
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🧐"
              },
              {
                "type": "text",
                "text": "只要打出",
                "wrap": True,
                "size": "sm",
                "margin": "none",
                "offsetBottom": "sm",
                "offsetTop": "none"
              },
              {
                "type": "separator"
              },
              {
                "type": "text",
                "text": "召喚錢錢管家",
                "size": "sm",
                "margin": "sm",
                "wrap": True,
                "offsetBottom": "sm",
                "offsetTop": "none",
                "weight": "bold"
              },
              {
                "type": "separator"
              },
              {
                "type": "text",
                "text": "魔法陣就會被召喚出來\n接下來只要按下按鈕再照著指示做就可以囉",
                "margin": "none",
                "size": "sm",
                "offsetTop": "sm",
                "offsetBottom": "sm",
                "wrap": True,
                "gravity": "center"
              }
            ]
          },
          {
            "type": "image",
            "url": "https://o.remove.bg/downloads/2f01c3eb-9908-4506-b1fb-20399384f1b8/image-removebg-preview.png",
            "margin": "lg",
            "align": "center",
            "size": "full",
            "aspectMode": "fit",
            "offsetTop": "xl"
          }
        ]
      },
      "styles": {
        "hero": {
          "backgroundColor": "#fefecd"
        },
        "body": {
          "backgroundColor": "#fefecd"
        }
      }
    }
  ]
}
  return contents



