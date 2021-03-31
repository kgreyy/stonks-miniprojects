from stockapi import * # from the stonks-api repo

if __name__ == '__main__':
    index = CompanyDir() # get a directory of all companies
    compOfficer = {}

    for comp in index.listing:
        compOfficer[comp['company']] = [roleOfficer[1] for roleOfficer in Company(comp['companyID'],only='o').officers] # map company to board
        break

    with open('edges.csv','w') as f:
        f.write('Source;Target\n')
        for company in compOfficer.keys():
            for officer in compOfficer[company]:
                f.write(f"{officer};{company}\n") # write contents out to a csv file
