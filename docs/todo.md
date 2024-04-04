# Tasks

- [x] Setup Django project skeleton with Pyenv + Poetry (SQLite DB for start) + requirements.txt auto generation <https://github.com/Ddedalus/poetry-auto-export>
- [ ] Create basic models (Account app): User, Organization, OrganizationUser
- [ ] Add DB seed for models <https://github.com/Brobin/django-seed>
- [ ] Create CRUD for Contexts
- [ ] Create CRUD for Website
- [ ] Add Website scrapping functionality <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>  (with depth limit and total pages per site limit - not to blow up the internet), maybe use Scrapy <https://alioguzhan.medium.com/how-to-use-scrapy-with-django-application-c16fabd0e62e>
- [ ] Add WebSite ScrappedPage content extraction with <https://github.com/buriy/python-readability>
- [ ] Add Celery workers (+ Redis) for Scrapping and Content Extraction
- [ ] Add Celery UI
- [ ] Add Celery Beat for periodic rescrapping new pages from the site
- [ ] Add WebSockets and realtime Scrapping progress indicator on WebSite page <https://channels.readthedocs.io/en/stable/>
- [ ] WebSockets can receive command to Start/Stop/Pause scrapping
- [ ] Add esbuild + npm + TablerUI <https://tabler.io/preview> to basic layout
- [ ] Add overmind + Procfile to run all processes
- [ ] Style existing CRUD pages with TablerUI
- [ ] Add Docker + Compose + VSCode Remote Container (switch to Container local development)
- [ ] Add PGVector DB into Dockerized setup, switch Django to PG
- [ ] Add Chat page with Fake AI hardcoded replies, full interactions and Messages persistency
- [ ] Add Unit testing
 	- [ ] Add basic Context, Website, Chat/Message CRUD test
 	- [ ] Add ScrappedPage+Readability tests
- [ ] RAG functionality
 	- [ ] Add AI Client to communicate with local Ollama server for embedding/completion
 	- [ ] Add command to persist all existing data to vectors storage
 	- [ ] Add automatic vectorization for all new saved searchable data
 	- [ ] Add relevant vector search in DB, trimming to LLM window limit, wrapping in Prompt
 	- [ ] Add real LLM interaction/responses in Chat
 	- [ ] Respect filters Context + Content Type
 	- [ ] Respect previous message history (keep prev summarized context)
 	- [ ] Add tests for RAG features with mocked LLM interaction
- [ ] Content from YouTube videos
  - [ ] CRUD video links
  - [ ] Worker to extract subtitles
  - [ ] Vector storage of the content
  - [ ] Generate content summary
  - [ ] Incorporate in RAG search and filters
- [ ] REST API
  - [ ] RDF CRUD to all existing Entities
  - [ ] RDF Search
  - [ ] Bruno API docs to API
  - [ ] Cover some APIs with Integrational test
- [ ] Django admin to all Entities (Super Admin user)
  - [ ] Change Organization to Entity should be a separate custom "Transfer to Org" action
  - [ ] Contexts should be proposed only in the current Entity Org scope
- [ ] Users + Organizations management
  - [ ] Registration login/password <https://builtwithdjango.com/blog/user-authentication>
  - [ ] Login
  - [ ] Forgot password
  - [ ] Sending confirmation emails + Mailcatcher
  - [ ] CRUD Organizations
  - [ ] CRUD Users in Organizations, Leave Org
  - [ ] User profile update
  - [ ] Org profile update
  - [ ] Permissions check to access only pages owned by Org you are member
- [ ] Audit microservice (Flask)
  - [ ] Flask microservice with basic HTTP endpoint
  - [ ] Add NATS to Docker
  - [ ] Flask NATS listener
  - [ ] Add Django decorator wrapper around AI call methods (with custom labels to differentiate), measure request/response data size, request duration
  - [ ] Send metrics from Django to NATS
  - [ ] Collect metrics on Flask side, persist in Postgres
  - [ ] API to generate report for Org for date range: total requests, total data size, min/max/median request duration, per label aggregation: request, data size, min/max/median request duration
  - [ ] API to generate CSV file with stats above (using Pandas)
  - [ ] Add link to get CSV on Django app Org page
  - [ ] API to generate SVG/image graph:  for Org for date range per label requests histogram
  - [ ] Display image on Org page
- [ ] Production deploy Docker image and app optimizations