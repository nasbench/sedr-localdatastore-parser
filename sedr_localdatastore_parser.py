import ast
import sys
import csv

mylist = []
filename = sys.argv[1]

# Extracting the contents from the leveldb csv file
with open(filename, "r") as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # Replacing the "true" and "false" statements now to avoid error when passing to the "ast.literal_eval"
            mylist.append(ast.literal_eval(row[1].replace('true', 'True').replace('false', 'False')))

with open("parsed_data.csv", "w", newline='', encoding='utf-8') as fi:
    f = csv.writer(fi)
    f.writerow(["actor_object_type", "path", "normalized_path", "sha2", "md5", "user_sid", "user_name", "user_domain", "pid", "tid", "modified", "created", "security_descriptor", "signature_company_name", "cmd_line", "original_name", "start_time", "childprocess_path", "childprocess_normalized_path", "childprocess_sha2", "childprocess_md5", "childprocess_user_sid", "childprocess_user_name", "childprocess_user_domain", "childprocess_session_id", "childprocess_pid", "childprocess_tid", "childprocess_modified", "childprocess_created", "childprocess_security_descriptor", "childprocess_signature_company_name", "childprocess_cmd_line", "childprocess_original_name", "childprocess_start_time", "reg_path", "reg_name", "reg_target_value", "reg_result_value", "file_path", "file_normalized_path", "file_security_descriptor", "file_size", "src_ip", "src_port", "dst_ip", "dst_port", "action", "type_id", "begin_time", "end_time"])

    for i in mylist:
        i = i.decode('utf-8')
        # Skipping "event_pkey" events for now
        if not "event_pkey" in i :
            i = ast.literal_eval(i)
            actor_object_type = i["artifacts"]["actor"]["object_type"]
            # This is used to ignore any garbage from the original leveldb csv file
            if actor_object_type == "process":
                path = i["artifacts"]["actor"]["path"]["value"][0]

                try:
                    normalized_path = i["artifacts"]["actor"]["normalized_path"]["value"][0]
                except:
                    normalized_path = ""
                
                try:
                    sha2 = i["artifacts"]["actor"]["sha2"]["value"][0]
                except:
                    sha2 = ""

                try:
                    md5 = i["artifacts"]["actor"]["md5"]["value"][0]
                except:
                    md5 = ""

                try:
                    user_sid = i["artifacts"]["actor"]["user_sid"]["value"][0]
                except:
                    user_sid = ""

                try:
                    user_name = i["artifacts"]["actor"]["user_name"]["value"][0]
                except:
                    user_name = ""
                
                try:
                    user_domain = i["artifacts"]["actor"]["user_domain"]["value"][0]
                except:
                    user_domain = ""

                pid = i["artifacts"]["actor"]["pid"]["value"][0]

                try:
                    tid = i["artifacts"]["actor"]["tid"]["value"][0]
                except:
                    tid = ""
                
                try:
                    modified = i["artifacts"]["actor"]["modified"]["value"]
                except:
                    modified = ""

                try:
                    created = i["artifacts"]["actor"]["created"]["value"]
                except:
                    created = ""
                
                try:
                    security_descriptor = i["artifacts"]["actor"]["security_descriptor"]["value"][0]
                except:
                    security_descriptor = ""
                
                try:
                    signature_company_name = i["artifacts"]["actor"]["signature_company_name"]["value"][0]
                except:
                    signature_company_name = ""

                try:
                    cmd_line = i["artifacts"]["actor"]["cmd_line"]["value"][0]
                except:
                    cmd_line = ""
                
                try:
                    original_name = i["artifacts"]["actor"]["original_name"]["value"][0]
                except:
                    original_name = ""
                
                try:
                    start_time = i["artifacts"]["actor"]["start_time"]
                except:
                    start_time = ""

                target_object_type = i["artifacts"]["target"]["object_type"]

                # RELATED TO TYPE ID 8001
                try:
                    childprocess_path = i["artifacts"]["target"]["path"]["value"][0]
                except:
                    childprocess_path = ""
                
                try:
                    childprocess_normalized_path = i["artifacts"]["target"]["normalized_path"]["value"][0]
                except:
                    childprocess_normalized_path = ""

                try:
                    childprocess_sha2 = i["artifacts"]["target"]["sha2"]["value"][0]
                except:
                    childprocess_sha2 = ""

                try:
                    childprocess_md5 = i["artifacts"]["target"]["md5"]["value"][0]
                except:
                    childprocess_md5 = ""

                try:
                    childprocess_user_sid = i["artifacts"]["target"]["user_sid"]["value"][0]
                except:
                    childprocess_user_sid = ""

                try:
                    childprocess_user_name = i["artifacts"]["target"]["user_name"]["value"][0]
                except:
                    childprocess_user_name = ""

                try:
                    childprocess_user_domain = i["artifacts"]["target"]["user_domain"]["value"][0]
                except:
                    childprocess_user_domain = ""

                try:
                    childprocess_session_id = i["artifacts"]["target"]["session_id"]["value"][0]
                except:
                    childprocess_session_id = ""

                try:
                    childprocess_pid = i["artifacts"]["target"]["pid"]["value"][0]
                except:
                    childprocess_pid = ""

                try:
                    childprocess_tid = i["artifacts"]["target"]["tid"]["value"][0]
                except:
                    childprocess_tid = ""

                try:
                    childprocess_modified = i["artifacts"]["target"]["modified"]["value"]
                except:
                    childprocess_modified = ""

                try:
                    childprocess_created = i["artifacts"]["target"]["created"]["value"]
                except:
                    childprocess_created = ""

                try:
                    childprocess_security_descriptor = i["artifacts"]["target"]["security_descriptor"]["value"][0]
                except:
                    childprocess_security_descriptor = ""

                try:
                    childprocess_signature_company_name = i["artifacts"]["target"]["signature_company_name"]["value"][0]
                except:
                    childprocess_signature_company_name = ""

                try:
                    childprocess_cmd_line = i["artifacts"]["target"]["cmd_line"]["value"][0]
                except:
                    childprocess_cmd_line = ""

                try:
                    childprocess_original_name = i["artifacts"]["target"]["original_name"]["value"][0]
                except:
                    childprocess_original_name = ""

                try:
                    childprocess_start_time = i["artifacts"]["target"]["start_time"]
                except:
                    childprocess_start_time = ""
                # RELATED TO TYPE ID 8001 [END]
                
                # RELATED TO TYPE ID 8006 [START]
                try:
                    reg_path = i["artifacts"]["target"]["path"]["value"][0]
                except:
                    reg_path = ""

                try:
                    reg_name = i["artifacts"]["target"]["name"]["value"][0]
                except:
                    reg_name = ""

                try:
                    reg_target_value = i["artifacts"]["target"]["data"]["value"][0]
                except:
                    reg_target_value = ""

                try:
                    reg_result_value = i["artifacts"]["result"]["data"]["value"][0]
                except:
                    reg_result_value = ""
                # RELATED TO TYPE ID 8006 [END]
                
                # RELATED TO TYPE ID 8003 [START]
                try:
                    file_path = i["artifacts"]["target"]["path"]["value"][0]
                except:
                    file_path = ""

                try:
                    file_normalized_path = i["artifacts"]["target"]["normalized_path"]["value"][0]
                except:
                    file_normalized_path = ""

                try:
                    file_security_descriptor = i["artifacts"]["target"]["security_descriptor"]["value"][0]
                except:
                    file_security_descriptor = ""

                try:
                    file_size = i["artifacts"]["target"]["size"]["value"][0]
                except:
                    file_size = ""
                # RELATED TO TYPE ID 8003 [END]

                # RELATED TO TYPE ID 8007 [START]
                try:
                    src_ip = i["artifacts"]["target"]["src_ip"]["value"][0]
                except:
                    src_ip = ""

                try:
                    src_port = i["artifacts"]["target"]["src_port"]["value"][0]
                except:
                    src_port = ""

                try:
                    dst_ip = i["artifacts"]["target"]["dst_ip"]["value"][0]
                except:
                    dst_ip = ""

                try:
                    dst_port = i["artifacts"]["target"]["dst_port"]["value"][0]
                except:
                    dst_port = ""
                # RELATED TO TYPE ID 8007 [END]
                
                action = i["action"][0]
                type_id = i["type_id"]["value"][0]
                
                try:
                    begin_time = i["begin_time"]["value"]
                except:
                    begin_time = ""

                try:
                    end_time = i["end_time"]["value"]
                except:
                    end_time = ""
                
                f.writerow([actor_object_type, path, normalized_path, sha2, md5, user_sid, user_name, user_domain, pid, tid, modified, created, security_descriptor, signature_company_name, cmd_line, original_name, start_time, childprocess_path, childprocess_normalized_path, childprocess_sha2, childprocess_md5, childprocess_user_sid, childprocess_user_name, childprocess_user_domain, childprocess_session_id, childprocess_pid, childprocess_tid, childprocess_modified, childprocess_created, childprocess_security_descriptor, childprocess_signature_company_name, childprocess_cmd_line, childprocess_original_name, childprocess_start_time, reg_path, reg_name, reg_target_value, reg_result_value, file_path, file_normalized_path, file_security_descriptor, file_size, src_ip, src_port, dst_ip, dst_port, action, type_id, begin_time, end_time])
