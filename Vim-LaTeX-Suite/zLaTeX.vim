" Vim settings for LaTeX


""""""""""""""""""""""""""""""""""""""""""""LaTeX-Suite"""""""""""""""""""""""""""""""""""""""""""""
" IMPORTANT: win32 users will need to have 'shellslash' set so that latex can be called correctly.
set shellslash

" IMPORTANT: grep will sometimes skip displaying the file name if you search in a singe file. This
" will confuse Latex-Suite. Set your grep program to always generate a file-name.
set grepprg=grep\ -nH\ $*

nnoremap <F6> :TTemplate<CR>

" General settings
let g:tex_flavor = 'latex'
let g:Tex_ViewRule_pdf = 'evince'
let g:pdf_previewer = 'evince'
let g:vimtex_view_method = 'evince'
let g:Tex_CompileRule_pdf = 'xelatex -interaction=nonstopmode $*'
let g:vimtex_quickfix_mode = 0
let g:Tex_Folding = 1
let g:Tex_DefaultTargetFormat ='pdf'
let g:Tex_FormatDependency_pdf ='pdf'
let g:Tex_MultipleCompileFormats ='pdf'
let g:Tex_GotoError = 0 " Do not jump errors

" Define some environments
"""""""""""""""""""""""theorem-like environments""""""""""""""""""""""""
" theorem
let g:Tex_Env_theorem = "\\begin{theorem}\<CR>\\label{th:<++>}\<CR><++>\<CR>\\end{theorem}\<CR><++>"
let g:Tex_Env_th = g:Tex_Env_theorem
" assumption
let g:Tex_Env_assumption = "\\begin{assumption}\<CR>\\label{asm:<++>}\<CR><++>\<CR>\\end{assumption}\<CR><++>"
let g:Tex_Env_asm = g:Tex_Env_assumption
" exercise
let g:Tex_Env_exercise = "\\begin{exercise}\<CR>\\label{exe:<++>}\<CR><++>\<CR>\\end{exercise}\<CR><++>"
let g:Tex_Env_exe = g:Tex_Env_exercise
" problem
let g:Tex_Env_problem = "\\begin{problem}\<CR>\\label{prob:<++>}\<CR><++>\<CR>\\end{problem}\<CR><++>"
let g:Tex_Env_prob = g:Tex_Env_problem
" conjecture
let g:Tex_Env_conjecture = "\\begin{conjecture}\<CR>\\label{conj:<++>}\<CR><++>\<CR>\\end{conjecture}\<CR><++>"
let g:Tex_Env_conj = g:Tex_Env_conjecture
" lemma
let g:Tex_Env_lemma = "\\begin{lemma}\<CR>\\label{lem:<++>}\<CR><++>\<CR>\\end{lemma}\<CR><++>"
let g:Tex_Env_lem = g:Tex_Env_lemma
" proposition
let g:Tex_Env_proposition = "\\begin{proposition}\<CR>\\label{prop:<++>}\<CR><++>\<CR>\\end{proposition}\<CR><++>"
let g:Tex_Env_prop = g:Tex_Env_proposition
" corollary
let g:Tex_Env_corollary = "\\begin{corollary}\<CR>\\label{coro:<++>}\<CR><++>\<CR>\\end{corollary}\<CR><++>"
let g:Tex_Env_coro = g:Tex_Env_corollary
" remark
let g:Tex_Env_remark = "\\begin{remark}\<CR>\\label{rem:<++>}\<CR><++>\<CR>\\end{remark}\<CR><++>"
let g:Tex_Env_rem = g:Tex_Env_remark
" definition
let g:Tex_Env_definition = "\\begin{definition}\<CR>\\label{def:<++>}\<CR><++>\<CR>\\end{definition}\<CR><++>"
let g:Tex_Env_def = g:Tex_Env_definition
" example
let g:Tex_Env_example = "\\begin{example}\<CR>\\label{exp:<++>}\<CR><++>\<CR>\\end{example}\<CR><++>"
let g:Tex_Env_exp = g:Tex_Env_example
" enumerate
let g:Tex_Env_enumerate = "\\begin{enumerate}\<CR>\\item <++>\<CR>\\end{enumerate}\<CR><++>"
let g:Tex_Env_enum = g:Tex_Env_enumerate
let g:Tex_Env_en = g:Tex_Env_enumerate
" itemize
let g:Tex_Env_itemize = "\\begin{itemize}\<CR>\\item <++>\<CR>\\end{itemize}\<CR><++>"
let g:Tex_Env_item = g:Tex_Env_itemize
let g:Tex_Env_it = g:Tex_Env_itemize
" bibtex
let g:Tex_Env_bibtex = "\\bibliography{<++>}<++>\<CR>\\bibliographystyle{plain}"
let g:Tex_Env_bib = g:Tex_Env_bibtex
let g:Tex_Env_ref = g:Tex_Env_bibtex
let g:Tex_Env_reference = g:Tex_Env_bibtex
" algorithm
let g:Tex_Env_algorithm = "%\\usepackage{algorithm, algpseudocode, algorithmicx}\<CR>\\begin{algorithm}[htbp!]\<CR>\\caption{\label{alg:<++>}<++>}\<CR>\\begin{algorithmic}[1]\<CR>\\State <++>\<CR>\\end{algorithmic}\<CR>\\end{algorithm}\<CR><++>"
let g:Tex_Env_alg = g:Tex_Env_algorithm
let g:Tex_Env_algo = g:Tex_Env_algorithm

""""""""""""""""""""""""""equation-like environments"""""""""""""""""""""
" equation
let g:Tex_Env_equation = "\\begin{equation}\<CR>\\label{eq:<++>}\<CR><++>\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_eq = g:Tex_Env_equation
" equation star (s for star)
let g:Tex_Env_equations = "\\begin{equation}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++>\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_eqs = g:Tex_Env_equations
" align
let g:Tex_Env_align = "\\begin{align}\<CR>\\label{eq:<++>}\<CR><++> &\\;=\\; <++> \\\\\<CR>\\label{eq:<++>}\<CR><++> &\\;=\\; <++>\<CR>\\end{align}\<CR><++>"
let g:Tex_Env_al = g:Tex_Env_align
let g:Tex_Env_aln = g:Tex_Env_align
" align star (s for star)
let g:Tex_Env_aligns = "\\begin{align}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++> &\\;=\\; <++> \\\\\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++> &\\;=\\; <++>\<CR>\\end{align}\<CR><++>"
let g:Tex_Env_als = g:Tex_Env_aligns
let g:Tex_Env_alns = g:Tex_Env_aligns
" gather
let g:Tex_Env_gather = "\\begin{gather}\<CR>\\label{eq:<++>}\<CR><++> \\\\\<CR><++> \<CR>\\end{gather}\<CR><++>"
let g:Tex_Env_gt = g:Tex_Env_gather
" gather star (s for star)
let g:Tex_Env_gathers = "\\begin{gather}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++> \\\\\<CR><++> \<CR>\\end{gather}\<CR><++>"
let g:Tex_Env_gts = Tex_Env_gathers
" split
let g:Tex_Env_esplit = "\\begin{equation}\<CR>\\label{eq:<++>}\<CR>\\begin{split}\<CR><++> &\\;=\\; <++> \\\\\<CR><++> &\\;=\\; <++>\<CR>\\end{split}\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_esp = g:Tex_Env_esplit
" split star (s for star)
let g:Tex_Env_esplits = "\\begin{equation}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR>\\begin{split}\<CR><++> &\\;=\\; <++> \\\\\<CR><++> &\\;=\\; <++>\<CR>\\end{split}\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_esps = g:Tex_Env_esplits
" cases
let g:Tex_Env_ecases = "\\begin{equation}\<CR>\\label{eq:<++>}\<CR>\\begin{cases}\<CR><++> & <++> \\\\\<CR><++> & <++>\<CR>\\end{cases}\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_ecs = g:Tex_Env_ecases
" cases star (s for star)
let g:Tex_Env_ecasess = "\\begin{equation}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR>\\begin{cases}\<CR><++> & <++> \\\\\<CR><++> & <++>\<CR>\\end{cases}\<CR>\\end{equation}\<CR><++>"
let g:Tex_Env_ecss = g:Tex_Env_ecasess
" empheq
let g:Tex_Env_empheq = "%\\usepackage{empheq}\<CR>\\begin{empheq}[left=\\empheqlbrace\\,]{align}\<CR>\\label{eq:<++>}\<CR><++> &\\;=\\; <++> \\\\\<CR>\\label{eq:<++>}\<CR><++> &\\;=\\; <++>\<CR>\\end{empheq}\<CR><++>"
let g:Tex_Env_eeq = g:Tex_Env_empheq
let g:Tex_Env_empheqs = "%\\usepackage{empheq}\<CR>\\begin{empheq}[left=\\empheqlbrace\\,]{align}\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++> &\\;=\\; <++> \\\\\<CR>%\\label{eq:}\<CR>\\nonumber\<CR><++> &\\;=\\; <++>\<CR>\\end{empheq}\<CR><++>"
let g:Tex_Env_eeqs = g:Tex_Env_empheqs

""""""""""""""""""""""""""environments for beamer"""""""""""""""""""""
" frame
let g:Tex_Env_frame = "\\begin{frame}\<CR>\\frametitle{<++>}\<CR><++>\<CR>\\end{frame}\<CR><++>"
let g:Tex_Env_fr = g:Tex_Env_frame
" columns
let g:Tex_Env_columns = "\\begin{columns}[T]\<CR>\\begin{column}{<++>\\textwidth}\<CR><++>\<CR>\\end{column}\<CR>\\begin{column}{<++>\\textwidth}\<CR><++>\<CR>\\end{column}\<CR>\\end{columns}\<CR><++>"
let g:Tex_Env_cols = g:Tex_Env_columns
" column
let g:Tex_Env_column = "\\begin{column}{<++>\\textwidth}\<CR><++>\<CR>\\end{column}\<CR><++>"
let g:Tex_Env_col = g:Tex_Env_column
""""""""""""""""""""""""""""""""""""""LaTeX-Suite ends""""""""""""""""""""""""""""""""""""""""""""""

" Press <leader>lb to compile and export a BibTeX file that contains only the cited terms according
" to the current aux. It calls the getbib script in ~/local/bin.
nmap <leader>lb  <esc><leader>ll<esc> :! getbib "%:t:r"<cr><cr>

"" Trim BibTeX files on save.
"function TrimBibTeX()
"    let save_cursor = getpos(".")
"    " keeppatterns prevents the strange pattern from polluting the search history.
"    silent! keeppatterns %s/\s*=\s*/\ =\ /g
"    "silent! keeppatterns %s/^\s*//
"    silent! let @/ = ""
"    call setpos('.', save_cursor)
"endfunction
"autocmd BufWrite *.bib :call TrimBibTeX()
