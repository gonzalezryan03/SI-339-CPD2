import csv
import pandas as pd
# Define the HTML template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Athlete Information</title>
</head>
<body>
    <header>
        <h1>Athlete: {athlete_name}</h1>
    </header>

    <main>
        <article>
            <div>
                <strong>Meet:</strong> <span>{meet}</span>
            </div>
            <div>
                <strong>Date:</strong> <span>{date}</span>
            </div>
            <div>
                <strong>Time:</strong> <span>{time}</span>
            </div>
            <div>
                <strong>Overall Place:</strong> <span>{overall_place}</span>
            </div>
        </article>
    </main>
</body>
</html>
'''

# Path to the uploaded CSV file
csv_file_path = 'athletes/womens_team/Cecilia DeGuzman21142897.csv'
html_output = ""
# Read the CSV, skipping the first two lines
df = pd.read_csv(csv_file_path, skiprows=4, header=0)

# Fill NaN values with 'Unknown' or appropriate default
df = df.fillna('Unknown')

for index, row in df.iterrows():
    athlete_name = row['Name']
    meet = row['Meet']
    date = row['Date']
    time = row['Time']
    overall_place = row['Overall Place']
    
    print(f"Athlete: {athlete_name}, Meet: {meet}, Date: {date}, Time: {time}, Overall Place: {overall_place}")
    # Populate the HTML template with data from CSV
    html_output += html_template.format(
        athlete_name=athlete_name,
        meet=meet,
        date=date,
        time=time,
        overall_place=overall_place
    )

    # Save the HTML to a file or print to check
    with open(f'{athlete_name}_info.html', 'w') as output_file:
        output_file.write(html_output)
