install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md
	cat ./Results/metrics.txt >> report.md
	
	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](./Results/model_results.png)' >> report.md
	
	cml comment create report.md
		
update-branch:
	git config --global user.name "abid"
	git config --global user.email "1abid@duck.com"
	git commit -am "Update with new results"
	git push --force origin HEAD:update

add-remote: 
	git remote add space https://kingabzpro:$HF@huggingface.co/spaces/kingabzpro/Drug-Classification

pull-push-hub: 
	git pull origin update
	git switch update
	git push --force space update:main

deploy: add-remote pull-push-hub

all: install format train eval update-branch deploy