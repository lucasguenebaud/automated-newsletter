import pandas as pd
from datetime import date
DATE = str(date.today().strftime('%b %Y'))

def make_entry(news, color):
    template_string = r"""<tr>
    <td style="font-family:'Open Sans', Arial, sans-serif; font-size:18px; line-height:22px; color:#FFFFFF; letter-spacing:2px; padding-bottom:12px;" valign="top" align="left">{text} <br> <a href="{link}" style="text-decoration:none;">{type}</a></td>
</tr>
<tr>
    <td class="em_h20" style="font-size:0px; line-height:0px; height:25px;" height="25">&nbsp;</td>
</tr>""".format(text=news.text, type=news.type, link=news.link, color=color)
    return template_string

def make_body(news_list):
    color_i = -1
    colors = ["#5FC3EB","#007EAF"]
    category_string = r"""
<tr>
<td style="padding:35px 70px 30px;" class="em_padd" valign="top" bgcolor="{color}" align="center"><table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
    <tbody><tr>
        <td style="font-family:'Open Sans', Arial, sans-serif; font-size:24px; font-weight:bold; line-height:30px; color:#FAEB46;" valign="top" align="center">{category}</td>
    </tr>
    <tr>
        <td style="font-size:0px; line-height:0px; height:15px;" height="15">&nbsp;</td>
        <!--—this is space of 15px to separate two paragraphs ---->
    </tr>
"""
    string = ""
    current_category = None
    for _,news in news_list.iterrows():
        if news.category is not current_category:
            if current_category is not None :
                string += "</tbody></table></td>\n</tr>\n"
            color_i = (color_i+1)%2
            string += category_string.format(category=news.category, color=colors[color_i])
            current_category = news.category
        string += make_entry(news, colors[color_i])
    string += "</tbody></table></td>\n</tr>\n"
    return string
        

def generate_html():
    pass

if __name__ == "__main__":
    news_df = pd.read_csv('news.csv').sort_values(by='category').reset_index(drop=True)
    string = make_body(news_df)

    f = open("template.html", "rt")
    page = f.read()
    page = page.replace("THISISWHERETHEMONTHGOES", DATE)
    page = page.replace("THISISWHERETHECONTENTGOES", string)
    f.close()

    f = open("newsletter.html", "wt")
    f.write(page)
    f.close()