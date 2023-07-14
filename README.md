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
