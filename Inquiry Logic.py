from graphviz import Digraph

dot = Digraph(comment='Cancer Inquiry Logic')


dot.node('A', 'Is there a cancer site?')
dot.node('B', 'Yes')
dot.node('C', 'No, end of inquiry')
dot.node('D', 'Cancer Site Details')
dot.node('E', 'Is this cancer primary or secondary (metastatic)?')
dot.node('F', 'Primary')
dot.node('G', 'Secondary (Metastatic)')
dot.node('H', 'Diagnosis method for the primary cancer')
dot.node('I', 'Treatment received for the primary cancer')
dot.node('J', 'Has the primary cancer recurred after treatment?')
dot.node('K', 'Yes')
dot.node('L', 'No')
dot.node('M', 'Recurrence Details: When did it recur?')
dot.node('N', 'Recurrence Diagnosis Method')
dot.node('O', 'Treatment received for the recurrence')
dot.node('P', 'What additional treatments are planned? [For Recurrence]')
dot.node('Q', 'Which primary site has this cancer metastasized from? [For Secondary]')
dot.node('R', 'Diagnosis method for the secondary cancer')
dot.node('S', 'Treatment received for the secondary cancer')
dot.node('T', 'What additional treatments are planned? [For Secondary]')
dot.node('U', 'Is there another cancer site?')
dot.node('V', 'Yes, provide details of next site')
dot.node('W', 'No, end of inquiry')


dot.edges(['AB', 'AC'])
dot.edge('B', 'D')
dot.edge('D', 'E')
dot.edges(['EF', 'EG'])
dot.edge('F', 'H')
dot.edge('H', 'I')
dot.edge('I', 'J')
dot.edges(['JK', 'JL'])
dot.edge('K', 'M')
dot.edge('M', 'N')
dot.edge('N', 'O')
dot.edge('O', 'P')
dot.edge('G', 'Q')
dot.edge('Q', 'R')
dot.edges(['RS', 'ST'])
dot.edge('T', 'U')
dot.edges(['UV', 'UW'])
dot.edge('V', 'D', constraint='false')  
dot.attr(label=r'\nCancer Inquiry Logic Tree with Separate Recurrence Branch')
dot.attr(fontsize='20')


dot.render('cancer_inquiry_logic_tree_separate_recurrence', view=True)
