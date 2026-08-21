DSA03 NLP Error Analysis — Code and Output Bundle

Contents
1. solve_doc.py — complete Python script used to generate the solved DOCX and execute the NLP examples.
2. outputs.txt — corresponding verified outputs for Questions 1–7.
3. DSA03-NLP_CO2_AT3_completed.docx — completed assessment document.

Run
python3 solve_doc.py

Required packages
sudo pip3 install python-docx nltk scikit-learn pandas

The script uses the supplied DOCX at /home/ubuntu/upload/DSA03-NLP_CO2_AT3.docx when run in the original sandbox. For use elsewhere, update INPUT and OUTPUT paths at the top of solve_doc.py. Dataset-specific sections are written so that BBCNews.csv or another named public corpus can be supplied by changing the dataset path and column name as indicated in the code.
