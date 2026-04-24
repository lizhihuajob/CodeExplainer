class CodeExplainApp {
    constructor() {
        this.data = null;
        this.currentLanguage = 'python';
        this.fuse = null;
        this.init();
    }

    async init() {
        await this.loadData();
        this.setupEventListeners();
        this.renderElementList();
        this.initSearch();
    }

    async loadData() {
        try {
            const response = await fetch('code.json');
            this.data = await response.json();
        } catch (error) {
            console.error('Failed to load data:', error);
            this.data = {
                glossary: {},
                languages: {
                    python: { name: 'Python', description: '', elements: [] },
                    cpp: { name: 'C++', description: '', elements: [] },
                    java: { name: 'Java', description: '', elements: [] }
                }
            };
        }
    }

    setupEventListeners() {
        const languageTabs = document.querySelectorAll('.language-tab');
        languageTabs.forEach(tab => {
            tab.addEventListener('click', (e) => {
                this.switchLanguage(e.target.dataset.language);
            });
        });

        const searchInput = document.getElementById('search-input');
        searchInput.addEventListener('input', (e) => {
            this.handleSearch(e.target.value);
        });

        const searchButton = document.getElementById('search-button');
        searchButton.addEventListener('click', () => {
            const searchInput = document.getElementById('search-input');
            this.handleSearch(searchInput.value);
        });

        document.addEventListener('click', (e) => {
            const searchResults = document.getElementById('search-results');
            const searchContainer = document.querySelector('.search-container');
            
            if (!searchContainer.contains(e.target)) {
                searchResults.classList.remove('active');
            }
        });

        const glossaryClose = document.getElementById('glossary-close');
        const glossaryModal = document.getElementById('glossary-modal');
        
        glossaryClose.addEventListener('click', () => {
            glossaryModal.classList.remove('active');
        });

        glossaryModal.addEventListener('click', (e) => {
            if (e.target === glossaryModal) {
                glossaryModal.classList.remove('active');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                glossaryModal.classList.remove('active');
            }
        });
    }

    switchLanguage(language) {
        this.currentLanguage = language;
        
        const languageTabs = document.querySelectorAll('.language-tab');
        languageTabs.forEach(tab => {
            if (tab.dataset.language === language) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });

        this.renderElementList();
        
        const detailView = document.getElementById('detail-view');
        detailView.innerHTML = `
            <div class="placeholder">
                <p>选择一个代码元素查看详细解释</p>
            </div>
        `;
    }

    renderElementList() {
        const elementList = document.getElementById('element-list');
        const elements = this.data.languages[this.currentLanguage]?.elements || [];

        if (elements.length === 0) {
            elementList.innerHTML = `
                <div class="element-item">
                    <div class="element-description">暂无数据</div>
                </div>
            `;
            return;
        }

        elementList.innerHTML = elements.map((element, index) => `
            <div class="element-item" data-id="${element.id}" style="animation-delay: ${index * 50}ms">
                <div class="element-name">${element.name}</div>
                <div class="element-description">${element.description}</div>
            </div>
        `).join('');

        const elementItems = elementList.querySelectorAll('.element-item');
        elementItems.forEach(item => {
            item.addEventListener('click', () => {
                this.showElementDetail(item.dataset.id);
                this.highlightElement(item);
            });
        });
    }

    highlightElement(activeItem) {
        const elementItems = document.querySelectorAll('.element-item');
        elementItems.forEach(item => {
            item.classList.remove('active');
        });
        activeItem.classList.add('active');
    }

    showElementDetail(elementId) {
        let element = null;
        let language = null;

        for (const [langKey, langData] of Object.entries(this.data.languages)) {
            const found = langData.elements.find(e => e.id === elementId);
            if (found) {
                element = found;
                language = langData.name;
                break;
            }
        }

        if (!element) return;

        const detailView = document.getElementById('detail-view');
        
        detailView.innerHTML = `
            <div class="detail-header">
                <h2 class="detail-name">${element.name}</h2>
                <span class="detail-language">${language}</span>
            </div>

            <div class="detail-section">
                <div class="section-header">
                    <div class="section-icon">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <line x1="12" y1="16" x2="12" y2="12"></line>
                            <line x1="12" y1="8" x2="12.01" y2="8"></line>
                        </svg>
                    </div>
                    <h3 class="section-title-detail">字面技术解释</h3>
                </div>
                <div class="section-content">
                    <div class="technical-explanation">
                        ${element.technical_explanation}
                    </div>
                </div>
            </div>

            <div class="detail-section">
                <div class="section-header">
                    <div class="section-icon" style="background-color: var(--success-color);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                            <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                    </div>
                    <h3 class="section-title-detail">想象隐喻解释</h3>
                </div>
                <div class="section-content">
                    <div class="metaphor-explanation">
                        <div class="metaphor-title">💡 生活化比喻</div>
                        ${element.metaphor_explanation}
                    </div>
                </div>
            </div>

            <div class="detail-section">
                <div class="section-header">
                    <div class="section-icon" style="background-color: var(--warning-color);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="16 18 22 12 16 6"></polyline>
                            <polyline points="8 6 2 12 8 18"></polyline>
                        </svg>
                    </div>
                    <h3 class="section-title-detail">代码示例</h3>
                </div>
                <div class="section-content">
                    ${element.examples.map(example => `
                        <div class="example-container">
                            <div class="example-header">📝 ${example.title}</div>
                            <pre class="example-code"><code>${this.escapeHtml(example.code)}</code></pre>
                        </div>
                    `).join('')}
                </div>
            </div>

            <div class="detail-section">
                <div class="section-header">
                    <div class="section-icon" style="background-color: var(--error-color);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <line x1="15" y1="9" x2="9" y2="15"></line>
                            <line x1="9" y1="9" x2="15" y2="15"></line>
                        </svg>
                    </div>
                    <h3 class="section-title-detail">语法注意事项</h3>
                </div>
                <div class="section-content">
                    <div class="syntax-notes">
                        <div class="syntax-title">⚠️ 重要提示</div>
                        <ul class="syntax-list">
                            ${element.syntax_notes.map(note => `<li>${note}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            </div>
        `;

        this.setupGlossaryLinks();
    }

    setupGlossaryLinks() {
        const glossaryTerms = document.querySelectorAll('.glossary-term');
        glossaryTerms.forEach(term => {
            term.addEventListener('click', (e) => {
                e.preventDefault();
                const termName = term.dataset.term;
                this.showGlossaryTerm(termName);
            });
        });
    }

    showGlossaryTerm(termName) {
        const term = this.data.glossary[termName];
        if (!term) return;

        const glossaryModal = document.getElementById('glossary-modal');
        const glossaryTitle = document.getElementById('glossary-title');
        const glossaryBody = document.getElementById('glossary-body');

        glossaryTitle.textContent = termName;
        
        glossaryBody.innerHTML = `
            <h4>定义</h4>
            <p>${term.definition}</p>
            
            ${term.characteristics && term.characteristics.length > 0 ? `
                <h4>特点</h4>
                <ul class="syntax-list">
                    ${term.characteristics.map(c => `<li>${c}</li>`).join('')}
                </ul>
            ` : ''}
            
            ${term.example ? `
                <div class="glossary-example">
                    <h4>示例</h4>
                    <pre><code>${this.escapeHtml(term.example)}</code></pre>
                </div>
            ` : ''}
            
            ${term.related_concepts && term.related_concepts.length > 0 ? `
                <h4>相关概念</h4>
                <p>${term.related_concepts.map(concept => 
                    `<a href="#" class="glossary-term" data-term="${concept}">${concept}</a>`
                ).join('、')}</p>
            ` : ''}
        `;

        glossaryModal.classList.add('active');
        this.setupGlossaryLinks();
    }

    initSearch() {
        const allElements = [];
        
        for (const [langKey, langData] of Object.entries(this.data.languages)) {
            for (const element of langData.elements) {
                allElements.push({
                    ...element,
                    language: langData.name,
                    languageKey: langKey
                });
            }
        }

        const options = {
            includeScore: true,
            threshold: 0.4,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
                { name: 'name', weight: 0.5 },
                { name: 'description', weight: 0.3 },
                { name: 'search_keywords', weight: 0.5 },
                { name: 'technical_explanation', weight: 0.2 }
            ]
        };

        this.fuse = new Fuse(allElements, options);
    }

    handleSearch(query) {
        const searchResults = document.getElementById('search-results');
        
        if (!query || query.trim() === '') {
            searchResults.classList.remove('active');
            return;
        }

        const results = this.fuse.search(query);
        
        if (results.length === 0) {
            searchResults.innerHTML = `
                <div class="search-result-item">
                    <div class="result-description">未找到相关结果</div>
                </div>
            `;
        } else {
            searchResults.innerHTML = results.slice(0, 10).map(result => {
                const item = result.item;
                return `
                    <div class="search-result-item" data-id="${item.id}">
                        <div class="result-name">${item.name}</div>
                        <span class="result-language">${item.language}</span>
                        <div class="result-description">${item.description}</div>
                    </div>
                `;
            }).join('');

            const resultItems = searchResults.querySelectorAll('.search-result-item');
            resultItems.forEach(item => {
                item.addEventListener('click', () => {
                    const elementId = item.dataset.id;
                    this.navigateToElement(elementId);
                    searchResults.classList.remove('active');
                    document.getElementById('search-input').value = '';
                });
            });
        }

        searchResults.classList.add('active');
    }

    navigateToElement(elementId) {
        let targetLanguage = null;
        let element = null;

        for (const [langKey, langData] of Object.entries(this.data.languages)) {
            const found = langData.elements.find(e => e.id === elementId);
            if (found) {
                targetLanguage = langKey;
                element = found;
                break;
            }
        }

        if (targetLanguage && element) {
            if (targetLanguage !== this.currentLanguage) {
                this.switchLanguage(targetLanguage);
            }

            setTimeout(() => {
                const elementItem = document.querySelector(`.element-item[data-id="${elementId}"]`);
                if (elementItem) {
                    elementItem.click();
                    elementItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }, 100);
        }
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new CodeExplainApp();
});
