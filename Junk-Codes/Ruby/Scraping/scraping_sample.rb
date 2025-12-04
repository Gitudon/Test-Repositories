require 'net/http'
require 'uri'
require 'nokogiri'

uri = URI.parse("https://example.com")
sleep 1
response = Net::HTTP.get_response(uri)
html = response.body

doc = Nokogiri::HTML(html)
h1_content = doc.css('h1')&.text
puts h1_content