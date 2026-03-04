# Rule-Based Expert System using Forward Chaining
rules = [
  (["fever","cough"],"flu"),
  (["flu"],"take rest"),
  (["rash"],"allergy"),
  (["allergy"],"take antihistamine"),
  (["fever","headache"],"viral infection"),
  (["viral_infection"],"drink fluids")]
def forward_chaining(facts,rules):
  inferred = set(facts)
  reasoning_log = []
  changed = True
  while changed:
    changed = False
    for rule in rules:
      conditions = rule[0]
      conclusion = rule[1]
      if all(condition in inferred for condition in conditions):
        if conclusion not in inferred:
          inferred.add(conclusion)
          reasoning_log.append(f"Rule applied: if {' and '.join(conditions)} then {conclusion}")
          changed = True
  return inferred, reasoning_log
print("Available symptoms: fever, cough, allergy")
user_input = input("Enter symptoms separated by commas: ")
facts = [fact.strip() for fact in user_input.split(",")]
results, log = forward_chaining(facts, rules)
if len(results) == len(facts):
    print("\nNot enough symptoms to infer a condition. Please enter more symptoms.")
print("\nFinal conclusions:")
for item in results:
  print("-",item)
print("\nReasoning steps:")
for step in log:
  print(step)
