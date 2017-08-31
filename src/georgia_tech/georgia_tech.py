import pandas as pd
import matplotlib.pyplot as plt

cat_url = '../../resources/google_s_and_p/CAT_data.csv'
cb_url = '../../resources/google_s_and_p/CB_data.csv'
dal_url = '../../resources/google_s_and_p/DAL_data.csv'
aal_url = '../../resources/google_s_and_p/AAl_data.csv'

cat_data = pd.read_csv(cat_url, index_col="Date", parse_dates=True)
cb_data = pd.read_csv(cb_url, index_col="Date", parse_dates=True)
dal_data = pd.read_csv(dal_url, index_col="Date", parse_dates=True)
aal_data = pd.read_csv(aal_url, index_col="Date", parse_dates=True)

cat_data = cat_data[["Close"]]['20160301':'20170301']
dal_data = dal_data[["Close"]]['20150601':'20160801']
aal_data = aal_data[["Close"]]['20130301':'20161101']

cat_data = cat_data.rename(columns = {"Close" : "Cat"})
dal_data = dal_data.rename(columns = {"Close" : "Dal"})
aal_data = aal_data.rename(columns = {"Close" : "Aal"})

new_data = cat_data.join(dal_data, how="inner")
new_data = new_data.join(aal_data, how="inner")
print(new_data)
new_data = new_data / new_data.ix[0, :]
print(new_data)

new_data.plot()
plt.show()

attr = "Close"

ranged_data = dal_data[["Open", "Low", "Close"]]['20160301':'20170301']

# one_time_data = dal_data[["Open", "Low", "Close"]]['20160301']

one_time_data = dal_data.loc['20160301': '20170301', ["Open", "Low", "Close"]]

print("one_time_dat: {}".format(dal_data.iloc[3]))

del dal_data["Name"]

new_data_frame = dal_data[["Open", "Close"]]

results = dal_data[['Open', 'Close']].apply(lambda item: item * 3)

part_dal_data = dal_data.loc['20160301': '20170301', ["Open"]]
part2_dal_data = dal_data.loc['20160601': '20170301', ["Open"]]
merge_dal_data = part_dal_data.merge(part2_dal_data)
indexes = merge_dal_data.index

print("results: {}, indexes: {}".format(merge_dal_data, indexes))

a = dal_data.iloc[3]

suma = a * 3

# new_data = dal_data[dal_data.Open > 12 and dal_data.Close > 12]

position = dal_data.iloc[1,1]
print("Position : {}".format(position))

print("Ranged data : {}".format(ranged_data))

print("One time data : {}".format(one_time_data))

data_frame_close = pd.DataFrame(index = aal_data.index)

data_frame_close = data_frame_close['20160301':'20170301']

data_frame_close["CAT"] = cat_data[attr]
data_frame_close["CB"] = cb_data[attr]
data_frame_close["DAL"] = dal_data[attr]
data_frame_close[["CAT", "CB", "DAL"]].plot()

plt.show()

print("data")
