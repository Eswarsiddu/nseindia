from dependencies.DataRequest import DataRequest
from dependencies.DataFormatter import DataFormatter
request = DataRequest(index=0)
dataformatter = DataFormatter(index=0)
data = dataformatter.update_data(data=request.request_data)