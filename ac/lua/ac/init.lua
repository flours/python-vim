local ac = {}
ac.ui = require('ac.ui')

-- for default options 

local _opt = {
   lang_commands={
     pypy='pypy',
     python='python3',
     javascript='node'
   },
   lang_extensions={
     py= 'pypy',
     js='javascript'
   },
   submit_lang_code = {
     pypy=4047,        --PyPy (7.3.0)
     python=4006,      --(Python (3.8.2))
     javascript=4030   --(Node.js 12.16.1)
   },
   ac_path=os.getenv("HOME").."/.ac"
}


ac._set_user = function(text,win)
  os.execute("mkdir -p ".._opt.ac_path)
  local f = io.open(_opt.ac_path.."/.ac.user","w")
  print(_opt.ac_path.."/.ac.user")
  f:write(text)
  f:close()
  ac.ui.close_win(win)
  print("set user name")
end

ac._set_pass = function(text,win)
  os.execute("mkdir -p ".._opt.ac_path)
  local f = io.open(_opt.ac_path.."/.ac.pass","w")
  f:write(text)
  f:close()
  ac.ui.close_win(win)
  print("set password")
end

ac._set_contest = function(text,win)
  os.execute("mkdir -p ".._opt.ac_path)
  local f = io.open(_opt.ac_path.."/.ac.contest","w")
  f:write(text)
  f:close()
  ac.ui.close_win(win)
  print("set contest")
end

ac.set_user = function()
  return ac.ui.create_prompt_window('user name?','require("ac")._set_user')
end

ac.set_pass = function()
  return ac.ui.create_prompt_window('password?','require("ac")._set_pass')
end

ac.set_contest = function()
  return ac.ui.create_prompt_window('contest?','require("ac")._set_contest')
end

ac.download_samples = function(problem)
  os.execute("mkdir -p ".._opt.ac_path)
  local f = io.open(_opt.ac_path.."/.ac.contest","r")
  local contest_name = f:read()
  f:close()
  local url = "https://atcoder.jp/contests/"..contest_name .."/tasks/"..contest_name.."_"..problem
  local dir_name = _opt.ac_path.."/"..contest_name.."/"..problem
  if vim.api.nvim_eval("isdirectory('"..dir_name.."')")==0 then
    os.execute("mkdir -p "..dir_name)
    os.execute("oj d -d "..dir_name.." "..url..">/dev/null 2>&1")
  end
end

ac.login = function()
  local f = io.open(_opt.ac_path.."/.ac.user","r")
  local user_name = f:read()
  f:close()

  f = io.open(_opt.ac_path.."/.ac.pass","r")
  local pass = f:read()
  f:close()
  pass = string.gsub(pass,"%%","\\%%")
  pass = string.gsub(pass,"#","\\#")
  vim.cmd("vs")
  vim.cmd("term oj login -u '"..user_name.."' -p '"..pass.."' https://atcoder.jp")
end

ac.test_with_lang = function(problem,lang)
  local f = io.open(_opt.ac_path.."/.ac.contest","r")
  local contest_name = f:read()
  f:close()
  local dir_name = _opt.ac_path.."/"..contest_name.."/"..problem
  ac.download_samples(problem)

  vim.cmd("vs")
  local cur_buf_file =vim.api.nvim_eval("expand('%:.')")
  vim.cmd("term oj test -d "..dir_name.." -c '".._opt.lang_commands[lang].." "..cur_buf_file.."'")
end

ac.test = function(problem)
  local ext = vim.api.nvim_eval("expand('%:e')")
  if _opt.lang_extensions[ext]~=nil then
    ac.test_with_lang(problem,_opt.lang_extensions[ext])
  else 
    print("please set language")
  end
end

ac.submit_with_lang  = function(problem,lang)
  local cur_buf_file =vim.api.nvim_eval("expand('%:.')")
  local f = io.open(_opt.ac_path.."/.ac.contest","r")
  local contest_name = f:read()
  f:close()
  local dir_name = _opt.ac_path.."/"..contest_name.."/"..problem
  local url = "https://atcoder.jp/contests/"..contest_name .."/tasks/"..contest_name.."_"..problem
  vim.cmd("vs")
  vim.cmd("term oj s -y -l ".._opt.submit_lang_code[lang].." "..url.." "..cur_buf_file)
end

ac.submit = function(problem)
  local ext = vim.api.nvim_eval("expand('%:e')")
  if _opt.lang_extensions[ext]~=nil then
    ac.submit_with_lang(problem,_opt.lang_extensions[ext],true)
  else 
    print("please set language")
  end
end

ac.setup = function(opt)
end

return ac
