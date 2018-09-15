import shutil, os, sys, threading, StringIO

from pinata import pinata

assert pinata.is_letter('a') == True
assert pinata.is_letter('1') == False
assert pinata.is_letter('#') == False

