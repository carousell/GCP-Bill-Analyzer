# GCP Bill Analyzer

Simple Python script to compare your GCP bills across months using the CSVs
exported from the billing console, across Projects, Services and SKUs.

- Input: GCP bills exported in CSV from the web console
- Output: CSV file `results.csv` with columns for cost of each Projects, Services, and SKUs


## Usage

### Using Pipenv

```
pipenv sync
python analyze.py <filename1> <filename2>
```

### Using Pip

```
pip install -r requirements.txt
python analyze.py <filename1> <filename2>
```

## Output

There is currently only 1 output file, `results.csv` which will be overwritten.

## License

Copyright 2020 Carousell

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
