local ui = {}

local window_list = {}

function shallowcopy(orig)
    local orig_type = type(orig)
    local copy
    if orig_type == 'table' then
        copy = {}
        for orig_key, orig_value in pairs(orig) do
            copy[orig_key] = orig_value
        end
    else -- number, string, boolean, etc
        copy = orig
    end
    return copy
end

local register_window = function(winid)
  window_list[winid]={}
end

local register_relation = function(winid,related_winid)
  table.insert(window_list[winid],related_winid)
end

ui.close_win = function(winid)
  for i=1 ,#window_list[winid] do
    vim.api.nvim_win_close(window_list[winid][i],true)
  end
  vim.api.nvim_win_close(winid,true)
end

local create_border_window = function(config,prompt)
  local opts = shallowcopy(config)
  opts.width=opts.width+2
  opts.height=opts.height+2
  opts.col=opts.col-1
  opts.row=opts.row-1

  local buf = vim.api.nvim_create_buf(false, true)
  local lines = {}
  table.insert(lines," " ..string.rep("-",(opts.width-2-string.len(prompt))/2) ..prompt ..string.rep("-",(opts.width-2-string.len(prompt))/2) .." ")
  for i = 1 ,opts.height-2 do
    table.insert(lines,"|" ..string.rep(" ",opts.width-2) .."|")
  end
  table.insert(lines," " ..string.rep("-",(opts.width-2)) .." ")
  vim.api.nvim_buf_set_lines(buf,0,-1,true,lines)
  vim.api.nvim_buf_set_option(buf,"buftype","nofile")
  local win = vim.api.nvim_open_win(buf, false, opts)
  vim.api.nvim_win_set_option(win, 'winhl', 'Normal:MyHighlight')
  return win
end

ui.create_prompt_window = function(prompt,callback_fn_name)
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_option(buf,"buftype","nofile")
  local width=30
  local opts = {relative='win', width=width, height=1,row=3, col=(vim.api.nvim_win_get_width(0)-width)/2, anchor= 'NW', style= 'minimal'}
  local border_win = create_border_window(opts,prompt)
  local win = vim.api.nvim_open_win(buf, true, opts)
  register_window(win)
  register_relation(win,border_win)
  vim.api.nvim_win_set_option(win, 'winhl', 'Normal:MyHighlight')
  vim.api.nvim_set_current_win(winid)
  vim.cmd("imap <silent><buffer> <esc> <esc><esc>")
  vim.api.nvim_buf_set_keymap(buf,'n','<esc>','[[<Cmd>lua require("ac").ui.close_win('..win..')<CR>]]',{noremap=true,silent=true})
  vim.api.nvim_buf_set_keymap(buf,'i','<cr>',"<esc><Cmd>call luaeval('"..callback_fn_name.. "(\"'.getline('.').'\","..win..")')<cr>",{noremap=true,silent=true,nowait=true})
  vim.cmd('call feedkeys("A","in")')
  return win
end

return ui
