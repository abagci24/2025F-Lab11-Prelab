class TabFileValidationError(Exception):
    pass


def validate_tab_file(file_path, expected_fields, required_pattern):
    
    try:
        with open(file_path,"r") as fid:
            tt = True
            count = 0
            for line in fid:
                satır = line.strip().split("\t")
                sayı1 = len(satır)
                count += 1

                if sayı1 != expected_fields:
                    raise TabFileValidationError( f"File path: {file_path}, Line {count}: Expected {expected_fields} fields, found {sayı1}")
                if required_pattern in line:
                    tt = False
            
            if tt:
                raise TabFileValidationError("File path: data.txt, No field contains required pattern 'missing_pattern'.")
            
        return "Tab-delimited file validation passed."
                
    except FileNotFoundError:
        return "File not found."
    
    

