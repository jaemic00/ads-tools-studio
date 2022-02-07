import sys
from bs4 import BeautifulSoup    

class Ad:
    def __init__(self,h1,h2,h3,ap,ctr,cost,cc,cr,convs):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.ap = ap
        self.ctr = ctr
        self.cost = cost
        self.cc = cc
        self.cr = cr
        self.convs = convs
        self.s_value = 0


def value_to_float(value):
    return float(str(value).strip('<value>').strip('</').strip('%'))

def give_s(ad,tc,cs,con_s,n,average):
    s = (ad.ap - average['ap']) + (ad.ctr - average['ctr']) + (tc - ad.cc) + (ad.cr - average['cr']) - (ad.cost/cs) + n*((ad.convs)/con_s)
    return s

def evaluate_group(xml_export):

    soup = BeautifulSoup(xml_export,"lxml")

    headlines = []
    headlines_2 = []
    headlines_3 = []
    aps = []
    ctrs = []
    costs = []
    conv_costs = []
    conv_rates = []
    convs = []

    for el in soup.find_all("cell"):
        if "Headline 1" in el.key:
            headlines.append(str(el.value).strip('<value>').strip('</').strip('%'))
        if "Headline 2" in el.key:
            headlines_2.append(str(el.value).strip('<value>').strip('</').strip('%'))
        if "Headline 3" in el.key:
            headlines_3.append(str(el.value).strip('<value>').strip('</').strip('%'))
        if "CTR" in el.key:
            ctrs.append(value_to_float(el.value)/100)
        if "Impr. (Top) %" in el.key:
            aps.append(value_to_float(el.value)/100)
        if "Cost" in el.key and "Cost / conv" not in el.key:
            costs.append(value_to_float(el.value))
        if "Cost / conv." in el.key:
            conv_costs.append(value_to_float(el.value))
        if "Conv. rate" in el.key:
            conv_rates.append(value_to_float(el.value) / 100)
        if "Conversions" in el.key:
            convs.append(value_to_float(el.value))

    n = len(headlines)    
    average = {
        'ap': sum(aps)/n,
        'ctr': sum(ctrs)/n,
        'cr' : sum(conv_rates)/n,
    }
    cs = sum(costs)
    con_s = sum(convs)

    ads = []
    for i in range(n):
        new_ad = Ad(headlines[i],headlines_2[i],headlines_3[i],aps[i],ctrs[i],costs[i],conv_costs[i],conv_rates[i],convs[i])
        ads.append(new_ad)
    for ad in ads:
        ad.s_value = give_s(ad,7.0,cs,con_s,n,average)
    
    ads.sort(key=lambda x: x.s_value, reverse=True)

    output = []
    for ad in ads:
        output.append({
            "ad": ad,
            "score": ad.s_value
        })
    return output
