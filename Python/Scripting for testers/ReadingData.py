import csv

#final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<Current runtime>]]

timing_data=[]
with open('TestTimingData.csv') as csv_file:
    file_reader=csv.reader(csv_file) 
    for row in file_reader:
        timing_data.append(row)

#Setting the values of 1st innerlist of both the list of lists
column_chart_data=[["Test Name","Diff from Avg"]]
table_data=[["Test Name","Run Time (s)"]]

#1: means traversing from row 1 till the end as the first row contains the header
for row in timing_data[1:]:
    test_name=row[0]
    #If a row has values missing in certain columns, it should be handle by the below 2 lines of code
    if not row[1] or not row[2]:
        continue
    current_run_time=float(row[1])
    average_run_time=float(row[2])
   
    diff_from_avg=average_run_time-current_run_time

    column_chart_data.append([test_name,diff_from_avg])
    table_data.append([test_name,current_run_time])

# print(column_chart_data)
# print(table_data)

#The below code is to link the above data to google charts API and generate charts
#the below code will help us create reusable templates
from string import Template

#""" wil help us generate new lines easily
html_string = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js">
<script type="text/javascript">
    google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart () {
        var data = google.visualization.arrayToDataTable([
         $labels,
         $data
         ],
         false); // 'false' means that the first row contains labels, not data.
       var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
          chart.draw(data);
    }
</script>
</head>
<body>
<div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

chart_data_str=''

#%s stands for substitution in our string
#\n for new line
#%row for inserting each row in that string
for row in column_chart_data[1:]:
    chart_data_str += '%s,\n'%row

#add header to complete the html
completed_html=html_string.substitute(labels=column_chart_data[0],data=chart_data_str)

with open('column_chart.html','w') as f:
    f.write(completed_html)