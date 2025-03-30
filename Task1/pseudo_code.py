# Initialize attributes
if isReturningUser:
    load_attributes_from_database()
else:
    initialize_defaults()  # active=True, confirmation=False, etc.

# Step 1: Greeting & Return Check
if not isReturningUser:
    print("Welcome! Let’s create your profile.")
    # Step 2: Collect Basic Info
    userName = input("Name: ")
    while True:
        age_input = input("Age: ")
        if age_input.isdigit() and int(age_input) >= 0:
            userAge = int(age_input)
            break
    if userAge < 18:
        guardian_input = input("Guardian consent? (yes/no): ")
        guardianConsent = guardian_input.lower() == "yes"
        if not guardianConsent:
            active = True  # Deactivate

# Step 3: Lifestyle Questions (encoded into lifestyleFlags)
if not isReturningUser or lifestyleFlags is None:
    livesAlone = ask_yes_no("Do you live alone?")
    isVegetarian = ask_yes_no("Are you vegetarian?")
    isReligious = ask_yes_no("Are you religious?")
    lifestyleFlags = (livesAlone << 2) | (isVegetarian << 1) | isReligious

# Step 4: Newsletter
if not isReturningUser or newsletterSubscription is None:
    newsletter_input = ask_yes_no("Subscribe to newsletter?")
    newsletterSubscription = newsletter_input

# Step 5: Language
if not isReturningUser or userLanguage is None:
    lang = input("Choose language (English/Spanish/French): ").capitalize()
    userLanguage = lang if lang in ["English", "Spanish", "French"] else "English"

# Step 6: Interests & Branching
if not isReturningUser or interests is None:
    interest = input("Interest (Product A, Product B, Service X): ")
    interests = interest
    if interest in ["Product A", "Product B"]:
        shippingAddress = input("Shipping address: ")
        shippingSpeed = input("Shipping speed (Standard/Express): ")
    elif interest == "Service X":
        serviceDate = input("Preferred date (YYYY-MM-DD): ")

# Step 7: Premium Support
premium_prompt = "Enable premium support?"
if isReturningUser and premiumSupportEnabled:
    premium_prompt += " (You previously used this)"
premiumSupportEnabled = ask_yes_no(premium_prompt)

# Step 8: Promo Code
promoCode = input("Promo code (or skip): ")
if promoCode:
    promoCodeValid = re.match(r'^[A-Z]{3}\d{4}[!@#$%^&*]{2}[a-z]{3}$', promoCode)
    while not promoCodeValid:
        promoCode = input("Invalid format. Re-enter or skip: ")
        if not promoCode:
            break
        promoCodeValid = re.match(...)

# Step 9: Summary & Confirmation
print_summary()  # Displays all attributes
confirmation = ask_yes_no("Confirm? (yes/no): ")
if confirmation:
    save_to_database()
else:
    exit()