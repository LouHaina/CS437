docker run --rm -t -p 8080:8080 -v license:/license \
  -e TOKEN= %%your token%% -e LICENSE_KEY= %%your license%% \
  platerecognizer/alpr-raspberry-pi
