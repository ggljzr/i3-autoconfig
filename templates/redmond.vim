set background=dark

hi clear
if exists("syntax on")
	syntax reset
endif

let g:colors_name = 'redmond'

hi Normal ctermfg=##vim_normal## ctermbg=None
hi Comment ctermfg=2 ctermbg=None
hi Constant ctermfg=Cyan ctermbg=None 
hi Operator ctermfg=Blue ctermbg=None
hi Statement ctermfg=Blue ctermbg=None cterm=bold
hi Special ctermfg=Yellow ctermbg=None cterm=bold
hi Visual ctermfg=Black ctermbg=2
hi Search ctermfg=Black ctermbg=2
hi Function ctermfg=Yellow ctermbg=None cterm=bold
hi LineNr ctermfg=Green ctermbg=None
hi Type ctermfg=green cterm=bold
hi Preproc ctermfg=magenta cterm=bold

hi VertSplit ctermfg=green ctermbg=green cterm=bold 
hi StatusLine ctermfg=green ctermbg=black
hi StatusLineNC ctermfg=darkblue ctermbg=white

hi TabLineSel ctermbg=green ctermfg=black cterm=bold
hi TabLine ctermbg=None ctermfg=##vim_normal## cterm=bold
hi TabLineFill ctermfg=grey cterm=bold

hi Title ctermfg=red
hi CursorLine ctermbg=darkRed ctermfg=green cterm=bold
hi NERDTreeDir ctermfg=Green
hi NERDTreeDirSlash ctermfg=Red cterm=bold
hi NERDTreeUp ctermfg=Yellow
hi NERDTreeHelp ctermfg=Cyan cterm = bold

hi Pmenu ctermfg=white ctermbg=DarkRed
hi PmenuSel ctermfg=black ctermbg=green cterm=bold

hi Question ctermfg=red
hi ModeMsg ctermfg=red
hi MoreMsg ctermfg=red
hi Underlined cterm=underline ctermfg=cyan

hi Directory ctermfg=green

hi StartifyHeader ctermfg=green
hi StarfiyPath ctermfg=green
hi StartifySlash ctermfg=red cterm=bold
