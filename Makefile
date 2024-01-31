install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

train:

	python train.py

eval:
	echo "## Model Metrics" > report.md
	cat Results/metrics.txt >> report.md
	
	echo "\n## Model Performance" >> report.md
	echo "Model performance metrics are on the plot below." >> report.md
	
	cml comment ![confusion matrix](Results/model_results.png) --md >> report.md
	
	cml comment create report.md

add-remote: 
	git remote add space https://kingabzpro:$HF@huggingface.co/spaces/kingabzpro/<app>

push-hub: 
	git push --force https://kingabzpro:$HF@huggingface.co/spaces/kingabzpro/<app> main

deploy: add-remote push-hub
		
all: install lint format deploy