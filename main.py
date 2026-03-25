from brochure import create_brochure

if __name__ == "__main__":
    company_name = input("Enter the company name: ")
    url = input("Enter the company website URL: ")
    print("\nGenerating brochure...\n")
    print(create_brochure(company_name, url))