def generate_test_case(requirement_text):
    lines = requirement_text.strip().split(".")
    test_cases = []
    tc_counter = 1
    
    for line in lines:
        line = line.strip().lower()
        if not line:
            continue
        
        if "login" in line or "email" in line:
            test_cases.append(f"TC_{tc_counter:03}: Enter valid email and password -> Login Successful")
            tc_counter += 1
            test_cases.append(f"TC_{tc_counter:03}: enter invalid password -> Show Error Message")
            tc_counter += 1
            test_cases.append(f"TC_{tc_counter:03}: Leave email field -> show required field message")
            tc_counter += 1
        if "submit" in line:
            test_cases.append(f"TC_{tc_counter:03}: click submit without filling fields -> show error message")
            tc_counter += 1
        if "password" in line:
            test_cases.append(f"TC_{tc_counter:03}: Enter special characters in password field -> reject login attempt")
            tc_counter += 1
    if not test_cases:
        test_cases.append("No specific testcases generated from the input.")
    return test_cases