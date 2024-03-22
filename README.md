A client repo for [Old Abe](https://github.com/drym-org/old-abe). This also doubles as a testbed for ABE workflows.

# Workflows

## Load template

This resets the accounting state of the repo.

```
$ ./load.sh <template>
```

... where `template` could be any folder in `templates/`. This restores the state of the `abe` folder to the contents of the template folder.

## New payment

```
$ ./in.py Sam 100
```

## New payout

```
$ ./out.py Sam 100
```

# Accounting Files

Old Abe uses many files in the `abe/` folder as the source of accounting information for the project. Here's a quick summary of what these files are for:

- advances.txt
  - A list of advances, that is, records of amounts that have been paid to contributors that was in excess of their attributive share for a given payment, when other contributors were unpayable.
- attributions.txt
  - The current project attributions, which must total to 100%.
- debts.txt
  - A list of current debts, that is, amounts that must be paid prior to making attributive payments.
- instruments.txt
  - Analogous to attributions.txt, but for "instruments" that faciliate delivery of the project (e.g. accounting, payment processors, DIA) which aren't part of the project itself. These are paid out first before each payment is accounted for the project.
- itemized_payments.txt
  - A breakdown of each payment recording the amount paid to the project vs the amount paid to instruments.
- payments
  - Files corresponding to each individual payment made to the project.
- payouts
  - Files corresponding to individual payments made to contributors by project trustees.
- price.txt
  - The amount up to which payments are considered compensation for use, and above which they are considered attributable investment.
- transactions.txt
  - A list of amounts from each payment that are owed to each contributor.
- unpayable_contributors.txt
  - A list of contributors (the name has to be the same one used in payments, etc.) who are currently unpayable. Any amount payable to them will be recorded as debt.
- valuation.txt
  - The current valuation of the project, used to determine the attributable share represented by investments.
