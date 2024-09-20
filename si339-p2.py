import csv

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

# Read the CSV and extract the relevant information
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV (assuming there's more than one row)
    for row in csv_reader:
        athlete_name = row['Athlete Name']  # Adjust based on actual column name
        meet = row['Meet']                  # Adjust based on actual column name
        date = row['Date']                  # Adjust based on actual column name
        time = row['Time']                  # Adjust based on actual column name
        overall_place = row['Overall Place']# Adjust based on actual column name

        # Populate the HTML template with data from CSV
        html_output = html_template.format(
            athlete_name=athlete_name,
            meet=meet,
            date=date,
            time=time,
            overall_place=overall_place
        )

        # Save the HTML to a file or print to check
        with open(f'{athlete_name}_info.html', 'w') as output_file:
            output_file.write(html_output)

        # Break after first row if we only want one athlete's info
        break