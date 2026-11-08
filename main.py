
import csv

KNOWLEDGE_BASE_FILE = "knowledge_base.csv"


# ==========================================
# 1. MAINTENANCE COST ESTIMATES
# ==========================================

# Hypothetical estimates in PKR for academic demonstration.

MAINTENANCE_COSTS = {
    "R1": {"inspection": 3000, "repair": 12000, "replacement": 45000},
    "R2": {"inspection": 3000, "repair": 15000, "replacement": 50000},
    "R3": {"inspection": 2500, "repair": 10000, "replacement": 35000},
    "R4": {"inspection": 2500, "repair": 8000, "replacement": 30000},
    "R5": {"inspection": 3000, "repair": 12000, "replacement": 40000},
    "R6": {"inspection": 2000, "repair": 7000, "replacement": 25000},
    "R7": {"inspection": 3000, "repair": 12000, "replacement": 50000},
    "R8": {"inspection": 2500, "repair": 10000, "replacement": 40000},
    "R9": {"inspection": 3000, "repair": 12000, "replacement": 45000},
    "R10": {"inspection": 2000, "repair": 7000, "replacement": 20000},
    "R11": {"inspection": 2000, "repair": 8000, "replacement": 25000},
    "R12": {"inspection": 2500, "repair": 7000, "replacement": 25000},
    "R13": {"inspection": 2000, "repair": 5000, "replacement": 15000},
    "R14": {"inspection": 2500, "repair": 10000, "replacement": 35000},
    "R15": {"inspection": 2000, "repair": 8000, "replacement": 30000}
}


# ==========================================
# 2. STAKEHOLDER PRIORITY WEIGHTS
# ==========================================

STAKEHOLDER_WEIGHTS = {
    "Safety Officer": 0.40,
    "Production Manager": 0.30,
    "Maintenance Manager": 0.20,
    "Finance Manager": 0.10
}


# Hypothetical impact ratings from 1 to 5.

STAKEHOLDER_IMPACT = {
    "R1": {"safety": 5, "production": 5, "maintenance": 4, "finance": 3},
    "R2": {"safety": 3, "production": 4, "maintenance": 4, "finance": 3},
    "R3": {"safety": 3, "production": 3, "maintenance": 4, "finance": 3},
    "R4": {"safety": 3, "production": 5, "maintenance": 4, "finance": 3},
    "R5": {"safety": 4, "production": 4, "maintenance": 4, "finance": 3},
    "R6": {"safety": 4, "production": 4, "maintenance": 4, "finance": 3},
    "R7": {"safety": 5, "production": 5, "maintenance": 4, "finance": 4},
    "R8": {"safety": 3, "production": 5, "maintenance": 4, "finance": 4},
    "R9": {"safety": 3, "production": 3, "maintenance": 4, "finance": 3},
    "R10": {"safety": 5, "production": 4, "maintenance": 4, "finance": 3},
    "R11": {"safety": 5, "production": 4, "maintenance": 4, "finance": 3},
    "R12": {"safety": 4, "production": 5, "maintenance": 4, "finance": 3},
    "R13": {"safety": 3, "production": 4, "maintenance": 3, "finance": 2},
    "R14": {"safety": 5, "production": 5, "maintenance": 4, "finance": 3},
    "R15": {"safety": 3, "production": 5, "maintenance": 4, "finance": 3}
}


# ==========================================
# 3. CERTAINTY FACTORS
# ==========================================

# Illustrative values, not statistically validated probabilities.

RULE_CERTAINTY_FACTORS = {
    "R1": 0.85,
    "R2": 0.80,
    "R3": 0.75,
    "R4": 0.80,
    "R5": 0.85,
    "R6": 0.80,
    "R7": 0.85,
    "R8": 0.80,
    "R9": 0.75,
    "R10": 0.80,
    "R11": 0.80,
    "R12": 0.80,
    "R13": 0.75,
    "R14": 0.80,
    "R15": 0.80
}


# ==========================================
# 4. EQUIPMENT OPTIONS
# ==========================================

equipment_options = {
    "1": "Electric Motor",
    "2": "Water Pump",
    "3": "Air Compressor"
}


# ==========================================
# 5. LOAD KNOWLEDGE BASE
# ==========================================

def load_knowledge_base():

    required_columns = [
        "rule_id",
        "equipment",
        "symptom",
        "possible_fault",
        "possible_cause",
        "maintenance_action",
        "priority",
        "source_id",
        "condition_fact",
        "conclusion_fact",
        "parent_fact"
    ]

    try:

        with open(
            KNOWLEDGE_BASE_FILE,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: Knowledge base CSV is empty.")
                return []

            # Remove spaces from CSV column headings.
            reader.fieldnames = [
                name.strip() if name else ""
                for name in reader.fieldnames
            ]

            missing_columns = [
                column for column in required_columns
                if column not in reader.fieldnames
            ]

            if missing_columns:
                print("Missing CSV columns:", missing_columns)
                return []

            rules = []

            for row in reader:

                cleaned_row = {}

                for key, value in row.items():

                    if key is not None and value is not None:
                        cleaned_row[key.strip()] = value.strip()

                # Skip completely empty rows.
                if not cleaned_row.get("rule_id"):
                    continue

                # Identify original diagnostic rules.
                condition = cleaned_row.get(
                    "condition_fact", ""
                ).strip()

                if not condition:

                    # Original rules require a symptom and possible fault.
                    if (
                        cleaned_row.get("equipment")
                        and cleaned_row.get("symptom")
                        and cleaned_row.get("possible_fault")
                    ):
                        rules.append(cleaned_row)

                else:

                    # Inference rules require a condition,
                    # conclusion and parent fact.
                    if (
                        cleaned_row.get("equipment")
                        and cleaned_row.get("conclusion_fact")
                        and cleaned_row.get("parent_fact")
                    ):
                        rules.append(cleaned_row)

            print("\nKnowledge base loaded successfully.")
            print("Total valid rules:", len(rules))

            return rules

    except FileNotFoundError:

        print("Error: knowledge_base.csv was not found.")
        print("Keep it in the same folder as main.py.")
        return []

    except Exception as error:

        print("Error reading knowledge base:", error)
        return []


# ==========================================
# 6. DISPLAY EQUIPMENT
# ==========================================

def display_equipment():

    print("\nSelect the equipment:")

    for number, name in equipment_options.items():
        print(number + ". " + name)

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice not in equipment_options:
        print("Invalid equipment selection.")
        return None

    return equipment_options[choice]


# ==========================================
# 7. GET AVAILABLE SYMPTOMS
# ==========================================

def get_available_symptoms(equipment, rules):

    symptoms = []

    for rule in rules:

        condition = rule.get("condition_fact", "").strip()

        # Only original diagnostic rules provide symptoms.
        if (
            rule.get("equipment") == equipment
            and not condition
        ):

            symptom = rule.get("symptom", "").strip()

            if symptom and symptom not in symptoms:
                symptoms.append(symptom)

    return symptoms


# ==========================================
# 8. GET USER SYMPTOMS
# ==========================================

def get_user_symptoms(available_symptoms):

    if not available_symptoms:
        print("No symptoms are available for this equipment.")
        return []

    print("\nAvailable symptoms:")

    for index, symptom in enumerate(available_symptoms, start=1):
        print(str(index) + ". " + symptom)

    print("\nYou can select multiple symptoms.")
    print("Separate symptom numbers with commas.")
    print("Example: 1,2")

    user_input = input("\nEnter symptom numbers: ").strip()

    selected_symptoms = []

    for number in user_input.split(","):

        number = number.strip()

        if not number.isdigit():
            print("Invalid input. Enter symptom numbers only.")
            return []

        number = int(number)

        if number < 1 or number > len(available_symptoms):
            print("Invalid symptom number.")
            return []

        symptom = available_symptoms[number - 1]

        if symptom not in selected_symptoms:
            selected_symptoms.append(symptom)

    if not selected_symptoms:
        print("No symptoms selected.")

    return selected_symptoms


# ==========================================
# 9. FORWARD CHAINING
# ==========================================

def forward_chaining(equipment, observed_symptoms, rules):

    known_facts = {
        "equipment": equipment,
        "symptoms": set(observed_symptoms),
        "possible_faults": set(),
        "confirmed_conditions": set(),
        "derived_facts": set(),
        "certainty_factors": {}
    }

    fired_rule_ids = set()
    fired_rules = []

    # Combine two positive certainty factors.
    def combine_cf(old_cf, new_cf):
        return old_cf + new_cf * (1 - old_cf)

    # Update certainty of a possible fault.
    def update_certainty(fault, new_cf):

        old_cf = known_facts["certainty_factors"].get(
            fault, 0.0
        )

        known_facts["certainty_factors"][fault] = combine_cf(
            old_cf, new_cf
        )

    # LEVEL 1: Original diagnostic rules.

    print("\n================================")
    print("LEVEL 1: INITIAL RULE MATCHING")
    print("================================")

    for rule in rules:

        condition = rule.get("condition_fact", "").strip()

        if condition:
            continue

        if (
            rule.get("equipment") == equipment
            and rule.get("symptom") in known_facts["symptoms"]
        ):

            rule_id = rule["rule_id"]

            fired_rule_ids.add(rule_id)
            fired_rules.append(rule)

            fault = rule["possible_fault"]

            known_facts["possible_faults"].add(fault)

            rule_cf = RULE_CERTAINTY_FACTORS.get(rule_id, 0.0)

            update_certainty(fault, rule_cf)

            print("Activated:", rule_id, "-", fault)

    # LEVEL 2: Ask for additional evidence.

    print("\n================================")
    print("LEVEL 2: ADDITIONAL EVIDENCE")
    print("================================")

    asked_conditions = set()

    for rule in rules:

        condition = rule.get("condition_fact", "").strip()
        parent = rule.get("parent_fact", "").strip()

        if not condition or not parent:
            continue

        if rule.get("equipment") != equipment:
            continue

        if parent not in known_facts["possible_faults"]:
            continue

        if condition in asked_conditions:
            continue

        asked_conditions.add(condition)

        print("\nHave you observed this condition?")
        print(condition)

        answer = input("Enter yes or no: ").strip().lower()

        if answer in ("yes", "y"):

            known_facts["confirmed_conditions"].add(condition)
            print("Additional condition confirmed.")

        else:

            print("Condition not confirmed.")

    # LEVEL 3: Additional inference rules.

    print("\n================================")
    print("LEVEL 3: INFERENCE RULES")
    print("================================")

    new_fact_found = True

    while new_fact_found:

        new_fact_found = False

        for rule in rules:

            rule_id = rule["rule_id"]

            if rule_id in fired_rule_ids:
                continue

            condition = rule.get("condition_fact", "").strip()
            conclusion = rule.get("conclusion_fact", "").strip()
            parent = rule.get("parent_fact", "").strip()

            if not condition or not conclusion or not parent:
                continue

            if (
                rule.get("equipment") == equipment
                and condition in known_facts["confirmed_conditions"]
                and parent in known_facts["possible_faults"]
            ):

                fired_rule_ids.add(rule_id)
                fired_rules.append(rule)

                known_facts["possible_faults"].add(conclusion)
                known_facts["derived_facts"].add(conclusion)

                parent_cf = known_facts["certainty_factors"].get(
                    parent, 0.0
                )

                rule_cf = RULE_CERTAINTY_FACTORS.get(rule_id, 0.0)

                derived_cf = parent_cf * rule_cf

                update_certainty(conclusion, derived_cf)

                print("Inference rule activated:", rule_id)
                print("New fact derived:", conclusion)

                new_fact_found = True

    return fired_rules, known_facts


# ==========================================
# 10. DISPLAY DIAGNOSIS RESULTS
# ==========================================

def display_results(equipment, observed_symptoms, fired_rules, known_facts):

    print("\n==============================================")
    print("       INDUSTRIAL FAULT DIAGNOSIS RESULTS")
    print("==============================================")

    print("\nSelected Equipment:")
    print(equipment)

    print("\nObserved Symptoms:")

    for symptom in observed_symptoms:
        print("- " + symptom)

    print("\n----------------------------------------------")
    print("INITIAL FACTS")
    print("----------------------------------------------")

    print("Equipment:", known_facts["equipment"])

    for symptom in sorted(known_facts["symptoms"]):
        print("Symptom:", symptom)

    print("\n----------------------------------------------")
    print("ACTIVATED RULES")
    print("----------------------------------------------")

    if fired_rules:

        for rule in fired_rules:

            print("\nRule ID:", rule["rule_id"])
            print("Condition:", rule.get("symptom", "") or
                  rule.get("condition_fact", ""))
            print("Possible Fault:", rule["possible_fault"])
            print("Possible Cause:", rule["possible_cause"])
            print("Maintenance Action:", rule["maintenance_action"])
            print("Priority:", rule["priority"])
            print("Source ID:", rule["source_id"])

    else:

        print("No rules were activated.")

    print("\n----------------------------------------------")
    print("POSSIBLE FAULTS")
    print("----------------------------------------------")

    if known_facts["possible_faults"]:

        for fault in sorted(known_facts["possible_faults"]):
            print("- " + fault)

    else:

        print("No possible faults identified.")

    print("\n----------------------------------------------")
    print("CONFIRMED ADDITIONAL CONDITIONS")
    print("----------------------------------------------")

    if known_facts["confirmed_conditions"]:

        for condition in sorted(known_facts["confirmed_conditions"]):
            print("- " + condition)

    else:

        print("No additional conditions confirmed.")

    print("\n----------------------------------------------")
    print("ADDITIONAL DERIVED FACTS")
    print("----------------------------------------------")

    if known_facts["derived_facts"]:

        for fact in sorted(known_facts["derived_facts"]):
            print("- " + fact)

    else:

        print("No additional facts derived.")

    print("\n----------------------------------------------")
    print("REASONING SUMMARY")
    print("----------------------------------------------")

    print("Inference Method: Forward Chaining")
    print("Step 1: Equipment and symptoms were received.")
    print("Step 2: The system matched symptoms with original rules.")
    print("Step 3: Matching rules identified possible faults.")
    print("Step 4: Additional evidence was requested from the user.")
    print("Step 5: Confirmed conditions were checked against inference rules.")

    print("\n==============================================")
    print("FINAL RESULT")
    print("==============================================")

    if known_facts["possible_faults"]:

        print("Diagnosis completed successfully.")
        print("The results are possible faults, not confirmed diagnoses.")

    else:

        print("No matching diagnosis could be generated.")

    print("\nIMPORTANT:")
    print("These results are decision-support suggestions only.")
    print("A qualified technician should inspect the equipment.")
    print("==============================================")


# ==========================================
# 11. BACKWARD CHAINING
# ==========================================

def run_backward_chaining(equipment, observed_symptoms, rules, known_facts):

    print("\n==============================================")
    print("BACKWARD CHAINING")
    print("==============================================")

    possible_faults = sorted(known_facts["possible_faults"])

    if not possible_faults:
        print("No possible faults available for testing.")
        return

    print("\nSelect a fault hypothesis to test:")

    for index, fault in enumerate(possible_faults, start=1):
        print(str(index) + ". " + fault)

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(possible_faults):
        print("Invalid choice.")
        return

    target_fault = possible_faults[choice - 1]

    print("\nSelected Hypothesis:")
    print(target_fault)

    print("\nChecking supporting evidence...")

    supporting_rules = []

    for rule in rules:

        if rule.get("equipment") != equipment:
            continue

        condition_fact = rule.get("condition_fact", "").strip()

        # Original diagnostic rules.
        if not condition_fact:

            if (
                rule.get("possible_fault") == target_fault
                and rule.get("symptom") in observed_symptoms
            ):

                supporting_rules.append(rule)

        # Additional inference rules.
        else:

            parent = rule.get("parent_fact", "").strip()
            condition = rule.get("condition_fact", "").strip()
            conclusion = rule.get("conclusion_fact", "").strip()

            if (
                parent in known_facts["possible_faults"]
                and condition in known_facts["confirmed_conditions"]
                and conclusion == target_fault
            ):

                supporting_rules.append(rule)

    print("\n==============================================")
    print("BACKWARD CHAINING RESULT")
    print("==============================================")

    if supporting_rules:

        print("Hypothesis:", target_fault)
        print("Status: SUPPORTED BY AVAILABLE EVIDENCE")

        print("\nSupporting Rules:")

        for rule in supporting_rules:

            print("\nRule ID:", rule["rule_id"])
            print("Condition:", rule.get("condition_fact", "") or
                  rule.get("symptom", ""))
            print("Possible Fault:", rule.get("possible_fault", ""))
            print("Possible Cause:", rule.get("possible_cause", ""))
            print("Source ID:", rule.get("source_id", ""))

    else:

        print("Hypothesis:", target_fault)
        print("Status: NOT SUPPORTED BY AVAILABLE EVIDENCE")

    print("\n==============================================")


# ==========================================
# 12. SAFETY ASSESSMENT
# ==========================================

def display_safety_alert(fired_rules):

    high_priority_rules = [
        rule for rule in fired_rules
        if rule["priority"].strip().lower() == "high"
    ]

    print("\n==============================================")
    print("SAFETY ASSESSMENT")
    print("==============================================")

    if high_priority_rules:

        print("\n!!! HIGH-PRIORITY SAFETY ALERT !!!")
        print("\nHigh-priority potential faults identified:")

        for rule in high_priority_rules:

            print("\nRule ID:", rule["rule_id"])
            print("Equipment:", rule["equipment"])
            print("Possible Fault:", rule["possible_fault"])
            print("Recommended Action:", rule["maintenance_action"])

        print("\nSAFETY RECOMMENDATION:")
        print("Follow the facility's safety procedures.")
        print("Arrange prompt inspection by qualified personnel.")
        print("Do not treat this result as a confirmed diagnosis.")

    else:

        print("\nNo high-priority rules were activated.")

    print("\nThis system does not automatically stop or control machinery.")
    print("==============================================")


# ==========================================
# 13. MAINTENANCE COST ESTIMATION
# ==========================================

def display_maintenance_costs(fired_rules):

    print("\n==============================================")
    print("MAINTENANCE COST ESTIMATION")
    print("==============================================")

    if not fired_rules:
        print("No maintenance costs available.")
        return

    for rule in fired_rules:

        rule_id = rule["rule_id"]
        costs = MAINTENANCE_COSTS.get(rule_id, {})

        print("\nRule ID:", rule_id)
        print("Possible Fault:", rule["possible_fault"])

        for cost_type in ("inspection", "repair", "replacement"):

            amount = costs.get(cost_type)

            if amount is None:
                print(cost_type.title() + " Cost: Not configured")
            else:
                print(
                    cost_type.title() + " Cost: PKR " + str(amount)
                )

    print("\nNOTE:")
    print("All displayed costs are hypothetical estimates in PKR.")
    print("They are provided for academic demonstration only.")
    print("Actual costs depend on equipment condition, parts and labour.")
    print("Inspection, repair and replacement are alternative scenarios.")


# ==========================================
# 14. STAKEHOLDER PRIORITY RESOLUTION
# ==========================================

def calculate_stakeholder_priority(fired_rules):

    print("\n==============================================")
    print("STAKEHOLDER-BASED WEIGHTED PRIORITY RANKING")
    print("==============================================")

    if not fired_rules:
        print("No activated rules to evaluate.")
        return

    results = []

    for rule in fired_rules:

        rule_id = rule["rule_id"]
        impacts = STAKEHOLDER_IMPACT.get(rule_id)

        if impacts is None:
            continue

        score = (
            impacts["safety"] * STAKEHOLDER_WEIGHTS["Safety Officer"]
            + impacts["production"] * STAKEHOLDER_WEIGHTS["Production Manager"]
            + impacts["maintenance"] * STAKEHOLDER_WEIGHTS["Maintenance Manager"]
            + impacts["finance"] * STAKEHOLDER_WEIGHTS["Finance Manager"]
        )

        results.append({
            "rule_id": rule_id,
            "possible_fault": rule["possible_fault"],
            "score": score,
            "impacts": impacts
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    print("\nStakeholder impact scores (1 to 5):")

    for item in results:

        print("\nRule ID:", item["rule_id"])
        print("Possible Fault:", item["possible_fault"])
        print("Safety Impact:", item["impacts"]["safety"])
        print("Production Impact:", item["impacts"]["production"])
        print("Maintenance Impact:", item["impacts"]["maintenance"])
        print("Finance Impact:", item["impacts"]["finance"])
        print("Weighted Priority Score:", round(item["score"], 2))

    print("\n==============================================")
    print("PRIORITY RANKING")
    print("==============================================")

    for position, item in enumerate(results, start=1):

        print(
            str(position) + ".",
            item["rule_id"],
            "-",
            item["possible_fault"],
            "| Score:",
            round(item["score"], 2)
        )

    if results:

        print("\nHighest combined stakeholder priority:")
        print(results[0]["rule_id"], "-", results[0]["possible_fault"])

    print("\nNOTE:")
    print("Scores use hypothetical stakeholder impact ratings.")
    print("This is a weighted decision-support ranking.")
    print("It does not automatically control machinery.")

    print("==============================================")


# ==========================================
# 15. CERTAINTY FACTOR ANALYSIS
# ==========================================

def display_certainty_factors(known_facts):

    print("\n==============================================")
    print("CERTAINTY FACTOR ANALYSIS")
    print("==============================================")

    certainty_factors = known_facts["certainty_factors"]

    if not certainty_factors:
        print("No certainty factors available.")
        return

    for fault, cf in sorted(certainty_factors.items()):

        percentage = cf * 100

        print("\nPossible Fault:", fault)
        print("Certainty Factor:", round(cf, 2))
        print("Evidence Support:", str(round(percentage, 2)) + "%")

    print("\nNOTE:")
    print("Certainty factors are illustrative rule-based scores.")
    print("They are not statistically validated probabilities.")

    print("==============================================")


# ==========================================
# 16. MAIN PROGRAM
# ==========================================

def main():

    print("==========================================")
    print(" INDUSTRIAL EQUIPMENT FAULT-DIAGNOSIS KBS")
    print("==========================================")

    # STEP 1: Load knowledge base.

    rules = load_knowledge_base()

    if not rules:
        print("\nThe system cannot start without valid rules.")
        return

    # STEP 2: Select equipment.

    equipment = display_equipment()

    if equipment is None:
        return

    # STEP 3: Get available symptoms.

    available_symptoms = get_available_symptoms(
        equipment,
        rules
    )

    # STEP 4: Get symptoms from user.

    selected_symptoms = get_user_symptoms(
        available_symptoms
    )

    if not selected_symptoms:
        return

    # STEP 5: Perform forward chaining.

    fired_rules, known_facts = forward_chaining(
        equipment,
        selected_symptoms,
        rules
    )

    # STEP 6: Display diagnosis results.

    display_results(
        equipment,
        selected_symptoms,
        fired_rules,
        known_facts
    )

    # STEP 7: Certainty factor analysis.

    display_certainty_factors(known_facts)

    # STEP 8: Safety assessment.

    display_safety_alert(fired_rules)

    # STEP 9: Maintenance cost estimation.

    display_maintenance_costs(fired_rules)

    # STEP 10: Stakeholder priority ranking.

    calculate_stakeholder_priority(fired_rules)

    # STEP 11: Backward chaining.

    if fired_rules:

        print("\nWould you like to test a fault hypothesis?")
        print("1. Yes - Backward Chaining")
        print("2. No - Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            run_backward_chaining(
                equipment,
                selected_symptoms,
                rules,
                known_facts
            )

        elif choice == "2":

            print("\nExiting the system.")

        else:

            print("\nInvalid choice. Exiting the system.")

    # STEP 12: Exit.

    print("\nThank you for using the KBS.")


if __name__ == "__main__":
    main()
