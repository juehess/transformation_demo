# Koordinatentransformationen in der Robotik

## 1 Einrichtung der Conda-Umgebung
Voraussetzung ist eine funktionierende und aktuelle `conda`-Installation. Wenn es noch nicht auf Ihrem System installiert ist, 
fahren Sie mit dem nächsten Abschnitt fort, andernfalls springen Sie direkt zu **1.2**.
### 1.1 Conda-Installation (Miniforge aka Mambaforge)
```
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3.sh
```
Akzeptieren Sie die Lizenzbedingungen und installieren Sie es an dem vorgeschlagenen Standardort. Auf die Frage, ob 
Miniforge3 initialisiert werden soll, geben Sie `yes` ein. Aktualisieren Sie dann Ihre bashrc:
```
source ~/.bashrc
```
Überprüfen Sie die korrekte Installation durch Ausführung:
```
which mamba
# should show: /home/<your username>/miniforge3/condabin/mamba
whih python
# should show: /home/<your username>/miniforge3/bin/python
```
Hinweis: Beachten Sie, dass dies den Standard-Python-Interpreter/die Installation ersetzt.
### 1.2 Umgebungserstellung
In den folgenden Codezeilen wird `conda` als ausführbare Datei verwendet, aber wenn Sie es installiert haben (z.B. durch Befolgen 
der Anweisungen in 1.1), können Sie es auch durch `mamba` ersetzen, das im Grunde das Gleiche tut, aber viel schneller.
```
conda env create -f conda-env.yaml
```
Dies kann je nach Ihrer Internetverbindung eine Weile dauern.
Nach Abschluss aktivieren Sie die Umgebung:
```
conda activate transform
```
## 2 Starten und Ausführen im Jupyter Notebook
```
jupyter notebook
```
