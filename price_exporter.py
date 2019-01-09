import json
from pprint import pprint

from openpyxl import Workbook

def get_diff(name, plan):
    return {"diff": [plan[0] - plan[1], plan[1] - plan[2]], "name": name}

def get_higher_diff(slot, phone1, phone2):
    if phone1["diff"][slot] < phone2["diff"][slot]:
        return phone2
    return phone1
    
if __name__ == "__main__":
    wb = Workbook()
    dest_filename = "prices.xlsx"
    ws1 = wb.active
    current_max_diffs = [{"diff":[0,0]},{"diff":[0,0]}]
    with open("price_list.json") as f:
        plans = json.load(f)
    for phone in plans:
        costs = [int(c[1:]) for c in plans[phone]]
        costs.insert(0, phone)
        ws1.append(costs)
        #cur_diff = get_diff(phone, costs)
        #for i in range(2):
        #    current_max_diffs[i] = get_higher_diff(i, current_max_diffs[i], cur_diff)
    #pprint(current_max_diffs)
    wb.save(filename=dest_filename)