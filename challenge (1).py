import csv
def get_csv_data(csv_file):
    list_of_dicts = []
   
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts

def count_high_stress_females(dataset):
    count = 0
    total_females = 0 
    for row in dataset:
        try:
            if row["Gender"].strip().lower() == "female":
                total_females += 1
                stress_level = float(row["Stress_Level(1-10)"])
                if stress_level > 6:
                    count += 1
        except:

            continue
        
    return count, total_females

def average_female_stress(dataset):
    total_stress = 0
    total_females = 0
    for row in dataset:
        try:
            if row["Gender"].strip().lower() == "female":
                stress = float(row["Stress_Level(1-10)"])
                total_stress += stress
                total_females += 1
        except:
            
            continue
       
    if total_females == 0:
        return 0
    return total_stress/total_females

def write_results(filename, stress_count, total_females, percentage):
    with open(filename, "w") as f:
        f.write("Female Stress Level Analysis:\n")
        f.write("Number of females: {total_females}")
        f.write(f"Females with stress levels > 6: {stress_count}")
        f.write(f"Percentage: {percentage}%")
    print(f"Results: {filename}")

if __name__ == "__main__": 
    dataset = get_csv_data("Mental_Health_and_Social_Media_Balance_Dataset.csv")

    stress_count, total_females = count_high_stress_females(dataset)

    if total_females > 0:
        percentage = (stress_count/total_females) * 100
    
    else:
        percentage = 0

    print("Total numbers of females: ", total_females)
    print("Females with stress levels > 6: ", stress_count)
    print("Percentage: ", percentage, "%")

    avg_stress = average_female_stress(dataset)
    print(f"Average stress levels for females: ", avg_stress)

    write_results("female_analysis.txt", stress_count, total_females, percentage)
